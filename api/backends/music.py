from api.backends.base import BaseBackend
from api.parsers.metacritic import MetacriticMusicParser

class MusicBackend(BaseBackend):
    """MusicBackend represents a music type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser = MetacriticMusicParser()

    def search(self, query):
        """search finds the result list in the HTML and builds return objects"""
        return self.parser.parse(query)
