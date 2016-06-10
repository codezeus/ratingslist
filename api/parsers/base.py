import requests
import bs4


class BaseParser:
    """BaseParser is an abstract method which parsers should inherit from.

    It provides a simple way to fetch a URL and parse the HTML for use in a
    parser type. Parsers can then use the BeautifulSoup API to parse nodes and
    extract any information needed.

    """
    def __init__(self):
        self.headers = {
            'User-Agent': ('Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) '
                           'Gecko/20110201')
        }

    def get_url(self):
        """get_url formats a URL for the request"""
        raise NotImplementedError

    def get_response(self, list_item):
        raise NotImplementedError

    def get_html(self):
        """get_html makes the request and returns a BeautifulSoup object"""
        r = requests.get(self.get_url(), headers=self.headers)
        return bs4.BeautifulSoup(r.text, 'html.parser')
