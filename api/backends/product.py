from api.backends.base import BaseBackend


class ProductBackend(BaseBackend):
    """ProductBackend represents a product type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser_class = None
