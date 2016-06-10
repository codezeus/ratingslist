from api.backends.base import BaseBackend


class PlaceBackend(BaseBackend):
    """PlaceBackend represents a place type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser_class = None
