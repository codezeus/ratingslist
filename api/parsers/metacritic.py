import urllib
from dateutil import parser as date_parser

from api.parsers.base import BaseParser
from api.types import is_numeric


class MetacriticParser(BaseParser):
    """MetacriticParser is an abstract class for fetching data from metacritic

    Most of the heavy lifting is done here with subclasses just needing to
    define their type.

    """
    base_url = 'http://www.metacritic.com'
    url = ('{base_url}/search/all/{query}/results?cats%5B{type}%5D=1'
           '&search_type=advanced')

    query = ''

    def parse(self, query):
        """parse makes the request, builds the HTML, and returns a response"""
        self.query = query

        html = self.get_html()

        results = []
        for item in html.find_all('li', {'class': 'result'}):
            results.append(self.get_response(item))

        return results

    def get_url(self):
        """set_url sets the current URL to query"""
        return self.url.format(
            base_url=self.base_url,
            query=urllib.quote_plus(self.query),
            type=self.type
        )

    def get_response(self, list_item):
        """get_response specifies the response object to return"""
        return {
            'title': self.get_title(list_item),
            'score': self.get_score(list_item),
            'link': self.get_link(list_item),
            'release_date': self.get_release_date(list_item),
        }

    def get_title(self, list_item):
        """get_title extracts the title from the resultset"""
        return list_item.find('h3').get_text()

    def get_link(self, list_item):
        """get_link extracts the link from the resultset"""
        return self.base_url + list_item.find('h3').find('a')['href']

    def get_release_date(self, list_item):
        """get_release_date extracts the release date"""
        date = None
        row = list_item.find('li', {'class': 'release_date'})
        if row:
            date = row.find('span', {'class': 'data'}).get_text()
        return date_parser.parse(date) if date else None

    def get_score(self, list_item):
        """get_score finds the proper score for the movie.

        We first try to get the user-based score since it is typically more
        aligned to the general public opinion rather than critics. If that
        doesn't exist then we try to get the critic score instead. If neither
        exist then we don't have a score attached to it.

        """
        user_score = list_item.find('span', {'class': 'textscore'})
        if user_score and is_numeric(user_score.get_text()):
            return float(user_score.get_text())

        critic_score = list_item.find('span', {'class': 'metascore_w'})
        if critic_score and is_numeric(critic_score.get_text()):
            return float(critic_score.get_text()) / 10.0

        return None


class MetacriticMovieParser(MetacriticParser):
    """MetacriticMovieParser searches for movies"""
    def __init__(self):
        MetacriticParser.__init__(self)
        self.type = 'movie'


class MetacriticMusicParser(MetacriticParser):
    """MetacriticMusicParser searches for albums"""
    def __init__(self):
        MetacriticParser.__init__(self)
        self.type = 'album'

    def response(self, list_item):
        """response overrides the parent response splitting name and artist"""
        response = MetacriticParser.response(self, list_item)
        title, artist = self.get_title(list_item).split(' - ')
        response['title'] = title
        response['artist'] = artist
        return response
