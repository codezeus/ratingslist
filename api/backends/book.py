from api.backends.base import BaseBackend


class BookBackend(BaseBackend):
    """BookBackend represents a book type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser_class = None
