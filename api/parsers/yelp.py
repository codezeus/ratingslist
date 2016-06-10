import urllib
from collections import namedtuple
# from dateutil import parser as date_parser

from api.parsers.base import BaseParser
from api.types import is_numeric


class YelpParser(BaseParser):
    """YelpParser is an abstract class for fetching data from Yelp"""
    base_url = 'http://www.yelp.com'
    url = '{base_url}/search?find_desc={description}&find_loc={location}'

    description = ''
    location = ''

    def parse(self, location, description):
        """parse makes the request, builds the HTML, and returns a response"""
        self.location = location
        self.description = description

        html = self.get_html()

        results = []
        for item in html.find_all('li', {'class': 'regular-search-result'}):
            results.append(self.get_response(item))

        return results

    def get_url(self):
        """set_url sets the current URL to query"""
        return self.url.format(
            base_url=self.base_url,
            description=urllib.quote_plus(self.description),
            location=urllib.quote_plus(self.location),
        )

    def get_response(self, list_item):
        """response specifies the response object to return"""
        return {
            'title': self.get_title(list_item),
            'link': self.get_link(list_item),
            'address': self.get_address(list_item),
            'phone': self.get_phone(list_item),
            'score': self.get_score(list_item),
        }

    def get_title(self, list_item):
        """get_title extracts the title from the resultset"""
        title = list_item.find('a', {'class': 'biz-name'}).find('span')
        return title.get_text()

    def get_link(self, list_item):
        """get_link extracts the link from the resultset"""
        link = list_item.find('a', {'class': 'biz-name'})
        return self.base_url + link.get('href')

    def get_phone(self, list_item):
        """get_phone extracts the title from the resultset"""
        phone = list_item.find('span', {'class': 'biz-phone'})
        return phone.get_text().strip()

    def get_address(self, list_item):
        """get_address break the address into a namedtuple"""
        Address = namedtuple('Address', ['addr', 'city', 'state', 'zip'])
        extract = [text for text in list_item.find('address').stripped_strings]

        # Sometimes a street address is not given
        if len(extract) == 1:
            addr, rest = None, extract[0]
        else:
            addr, rest = extract

        city, rest = rest.split(',')
        state, zip = rest.strip().split(' ')
        return Address(addr, city, state, zip)

    def get_score(self, list_item):
        """get_score finds the proper score for the place"""
        stars = list_item.find('div', {'class': 'rating-large'})
        if stars:
            split_class = stars.find('i').get('title').split(' ')
            if split_class and is_numeric(split_class[0]):
                return float(split_class[0]) * 2.0
        return None
