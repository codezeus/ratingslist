from api.backends.base import BaseBackend
from api.types import is_numeric

class MovieBackend(BaseBackend):
    """MovieBackend represents a movie type.

    A movie scrapes metacritic.com finding movies that match a given query.
    Movies have titles, scores, and a link to the dedicated page.

    """
    def __init__(self):
        BaseBackend.__init__(self)

        self.base_url = 'http://www.metacritic.com'
        self.url = '{base_url}/search/all/{query}/results?cats%5Bmovie%5D=1&search_type=advanced'

    def search(self, query):
        """search finds the result list in the HTML and builds return objects"""
        html = self.get_html(query)

        results = []
        for item in html.find_all('li', { 'class': 'result' }):
            results.append({
                'title': self.get_title(item),
                'score': self.get_score(item),
                'link': self.get_link(item),
            })

        return results

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
