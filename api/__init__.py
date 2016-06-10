import os


class Client:
    """Client is the main entrypoint for all API interactions.

    Backends can be called through dot notation to make API calls. For
    example, if you want to find movies then you can call:

        import api
        client = api.get_client()
        matches = client.movie.search('The Room')

    Invalid backends will raise an AttributeError.

    """
    invalid_attrs = ['base']

    @classmethod
    def get_new(cls):
        return cls()

    def __dir__(self):
        return [b.split('.')[0] for b in os.listdir('./api/backends/') if not
                b.startswith('_') and b.split('.')[0] not in
                self.invalid_attrs]

    def __getattr__(self, attr):
        if attr in self.invalid_attrs:
            raise AttributeError('API does not have backend "%s"' % attr)

        try:
            cls = '{}Backend'.format(attr.title())
            module = __import__('api.backends.{}'.format(attr), fromlist=[cls])
            return getattr(module, cls)()
        except ImportError:
            raise AttributeError('API does not have backend "%s"' % attr)


def get_client():
    """get_client returns a new instance of an API client"""
    return Client.get_new()

__all__ = ['get_client']
