from api.backends.base import BaseBackend


class RecipeBackend(BaseBackend):
    """RecipeBackend represents a recipe type"""
    def __init__(self):
        BaseBackend.__init__(self)
        self.parser_class = None
