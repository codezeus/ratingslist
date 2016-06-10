class BaseBackend:
    """BaseBackend is an abstract backend which backends should inherit from"""
    parser_class = None

    def get_parser_class(self):
        """get_parser_class attempts to find the attached parser class. If it
        can't then it throws an error

        """
        if not self.parser_class:
            raise AttributeError(("'%s' should either include the "
                                  "`parser_class` attribute, or override the "
                                  "`get_parser_class()` method."
                                  % self.__class__.__name__))
        return self.parser_class

    def search(self, *args, **kwargs):
        """search finds the result list in the HTML and builds a response"""
        return self.get_parser_class().parse(*args, **kwargs)
