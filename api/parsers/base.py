import requests, urllib, bs4

class BaseParser:
    """BaseParser is an abstract method which parsers should inherit from.

    It provides a simple way to fetch a URL and parse the HTML for use in an
    parser type. Items can then use the BeautifulSoup API to parse nodes and
    extract any information needed.

    """
    def __init__(self):
        self.url = ''
        self.base_url = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101'
        }

    def get_url(self, query):
        """get_url formats a URL for the request"""
        query_string = urllib.quote_plus(query)
        return self.url.format(base_url=self.base_url, query=query_string)

    def get_html(self, query):
        """get_html makes the request and returns a BeautifulSoup object"""
        r = requests.get(self.get_url(query), headers=self.headers)
        return bs4.BeautifulSoup(r.text, 'html.parser')