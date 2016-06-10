from api.backends.base import BaseBackend
from api.parsers.metacritic import MetacriticMovieParser


class MovieBackend(BaseBackend):
    """MovieBackend represents a movie type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser_class = MetacriticMovieParser()
