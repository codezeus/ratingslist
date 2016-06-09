from api.backends.base import BaseBackend
from api.parsers.metacritic import MetacriticMovieParser

class MovieBackend(BaseBackend):
    """MovieBackend represents a movie type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser = MetacriticMovieParser()

    def search(self, query):
        """search finds the result list in the HTML and builds return objects"""
        return self.parser.parse(query)
