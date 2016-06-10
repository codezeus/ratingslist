from api.backends.base import BaseBackend
from api.parsers.amazon import AmazonParser


class ProductBackend(BaseBackend):
    """ProductBackend represents a product type"""
    parser_class = AmazonParser()
