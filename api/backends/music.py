from api.backends.base import BaseBackend
from api.parsers.metacritic import MetacriticMusicParser


class MusicBackend(BaseBackend):
    """MusicBackend represents a music type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser_class = MetacriticMusicParser()
