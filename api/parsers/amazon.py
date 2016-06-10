import urllib

from api.parsers.base import BaseParser
from api.types import is_numeric


class AmazonParser(BaseParser):
    """AmazonParser is an abstract class for fetching data from Amazon"""
    base_url = 'https://www.amazon.com'
    url = '{base_url}/s/?url=search-alias%3Daps&field-keywords={query}'

    query = ''

    def parse(self, query):
        """parse makes the request, builds the HTML, and returns a response"""
        self.query = query

        html = self.get_html()

        results = []
        for item in html.find_all('li', {'class': 's-result-item'}):
            results.append(self.get_response(item))

        return results

    def get_url(self):
        """set_url sets the current URL to query"""
        return self.url.format(
            base_url=self.base_url,
            query=urllib.quote_plus(self.query),
        )

    def get_response(self, list_item):
        """response specifies the response object to return"""
        return {
            'title': self.get_title(list_item),
            'link': self.get_link(list_item),
            'score': self.get_score(list_item),
        }

    def get_title(self, list_item):
        """get_title extracts the title from the resultset"""
        title = list_item.find('h2', {'class': 's-access-title'})
        return title.get_text()

    def get_link(self, list_item):
        """get_link extracts the link from the resultset"""
        link = list_item.find('a', {'class': 's-access-detail-page'})
        return link.get('href')

    def get_score(self, list_item):
        """get_score finds the proper score for the product"""
        stars = list_item.find('i', {'class': 'a-icon-star'})
        if stars:
            alt_text = stars.find('span', {'class': 'a-icon-alt'})
            if alt_text:
                score = alt_text.get_text().split(' ')[0]
                if is_numeric(score):
                    return float(score) * 2.0
        return None
