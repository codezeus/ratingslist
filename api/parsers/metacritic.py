from api.parsers.base import BaseParser
from api.types import is_numeric

class MetacriticParser(BaseParser):
    """MetacriticParser is an abstract class for fetching data from metacritic

    Most of the heavy lifting is done here with subclasses just needing to
    define their type.

    """
    def __init__(self):
        BaseParser.__init__(self)

        self.type = ''
        self.base_url = 'http://www.metacritic.com'
        self.url = '{base_url}/search/all/{query}/results?cats%5B{type}%5D=1&search_type=advanced'

    def parse(self, query):
        """parse makes the request, builds the HTML, and returns the response"""
        self.set_url(query)
        html = self.get_html(query)

        results = []
        for item in html.find_all('li', { 'class': 'result' }):
            results.append({
                'title': self.get_title(item),
                'score': self.get_score(item),
                'link': self.get_link(item),
            })

        return results

    def set_url(self, query):
        """set_url sets the current URL to query"""
        self.url = self.url.format(
            base_url=self.base_url,
            query=query,
            type=self.type
        )

    def get_title(self, list_item):
        """get_title extracts the title from the resultset"""
        return list_item.find('h3').get_text()

    def get_link(self, list_item):
        """get_link extracts the link from the resultset"""
        return self.base_url + list_item.find('h3').find('a')['href']

    def get_score(self, list_item):
        """get_score finds the proper score for the movie.

        We first try to get the user-based score since it is typically more
        aligned to the general public opinion rather than critics. If that
        doesn't exist then we try to get the critic score instead. If neither
        exist then we don't have a score attached to it.

        """
        user_score = list_item.find('span', { 'class': 'textscore' })
        if user_score and is_numeric(user_score.get_text()):
            return float(user_score.get_text())

        critic_score = list_item.find('span', { 'class': 'metascore_w' })
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
