import requests, urllib, bs4

class BaseBackend:
    """BaseBackend is an abstract method which backends should inherit from"""
    def __init__(self):
        self.parser = None

    def search(self, query):
        """search should be implemented in the backend itself"""
        raise NotImplementedError
