from book import Book
from movie import Movie
from music import Music
from place import Place
from recipe import Recipe
from product import Product

class API:
    """API is the basic entrypoint to the API

    It is mainly used for the search method which will determine the item to
    look up and return the search results from the relevant API.

    """
    def search(self, category, query):
        """search looks up the type of request and sends the query to the
        item's search method

        """
        endpoint = None
        if category == 'book':
            endpoint = Book()
        elif category == 'movie':
            endpoint = Movie()
        elif category == 'music':
            endpoint = Music()
        elif category == 'place':
            endpoint = Place()
        elif category == 'recipe':
            endpoint = Recipe()
        elif category == 'product':
            endpoint = Product()
        else:
            raise Exception('Invalid type requested')

        return endpoint.search(query)
