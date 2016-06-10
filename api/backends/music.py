from api.backends.base import BaseBackend
from api.parsers.metacritic import MetacriticMusicParser


class MusicBackend(BaseBackend):
    """MusicBackend represents a music type"""
    parser_class = MetacriticMusicParser()
