class BaseBackend:
    """BaseBackend is an abstract method which backends should inherit from"""
    def __init__(self):
        self.parser_class = None

    def search(self, query):
        """search finds the result list in the HTML and builds a response"""
        return self.parser_class.parse(query)
