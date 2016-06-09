from api.backends.base import BaseBackend

class PlaceBackend(BaseBackend):
    def __init__(self):
        BaseBackend.__init__(self)

        self.base_url = ''
        self.url = ''

    def search(self, query):
        """search finds the result list in the HTML and builds return objects"""
        html = self.get_html(query)

        results = []
        return results
