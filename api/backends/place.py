from api.backends.base import BaseBackend
from api.parsers.yelp import YelpParser


class PlaceBackend(BaseBackend):
    """PlaceBackend represents a place type"""
    parser_class = YelpParser()
