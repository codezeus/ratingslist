from api.backends.base import BaseBackend
from api.parsers.metacritic import MetacriticMovieParser


class MovieBackend(BaseBackend):
    """MovieBackend represents a movie type"""
    parser_class = MetacriticMovieParser()
