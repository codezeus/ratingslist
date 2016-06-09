# Ratings List

Ratings List is a single source for people to collect the things they have
tried / done and attach a numerical rating to them. This reference allows
people to quickly find the things they liked and notes about them.

## Categories

To make this easy at first, we will provide a list of broad categories that
users can select from. In the future we may be able to add custom categories
but it will need to be thought about since my idea involves API endpoints. The
standard categories should be:

- Book
- Recipe
- Movie
- Music
- Place
- Product

## API Lookups

For each of the categories, I would like to implement API searches to give a
basis for autocompletion and comparison. For instance, when a user is entering
a new album it will crawl metacritic and find the album with rating
information and anything else we need. The following APIs / websites can be
used to get info:

- Book: goodreads.com
- Recipe: not sure yet...
- Movie: metacritic.com
- Music: metacritic.com
- Place: yelp.com
- Product: amazon.com

We don't need an API for these really. We can use requests with beautiful soup
to scrape results.

## Using the API

This is a major work in progress but it is working something like this so far:

```
>>> import api
>>> client = api.get_client()
>>> client.movie.search('The Room')
[{'score': 7.1, 'link': u'http://www.metacritic.com/movie/green-room', 'title': u'Green Room'},
 {'score': 8.4, 'link': u'http://www.metacritic.com/movie/room-2015', 'title': u'Room'}, {'scor
e': 7.8, 'link': u'http://www.metacritic.com/movie/the-forbidden-room', 'title': u'The Forbidde
n Room'}, {'score': 5.7, 'link': u'http://www.metacritic.com/movie/the-keeping-room', 'title': 
u'The Keeping Room'}, {'score': 5.4, 'link': u'http://www.metacritic.com/movie/war-room', 'titl
e': u'War Room'}, {'score': 5.0, 'link': u'http://www.metacritic.com/movie/the-room', 'title': 
u'The Room'}, {'score': 8.6, 'link': u'http://www.metacritic.com/movie/panic-room', 'title': u'
Panic Room'}, {'score': 6.2, 'link': u'http://www.metacritic.com/movie/room-237', 'title': u'Ro
om 237'}, {'score': None, 'link': u'http://www.metacritic.com/movie/the-dead-room', 'title': u'
The Dead Room'}, {'score': 7.9, 'link': u'http://www.metacritic.com/movie/a-room-with-a-view', 
'title': u'A Room with a View'}, {'score': 3.9, 'link': u'http://www.metacritic.com/movie/the-m
aids-room', 'title': u"The Maid's Room"}, {'score': 2.2, 'link': u'http://www.metacritic.com/mo
vie/boiler-room', 'title': u'Boiler Room'}, {'score': 4.9, 'link': u'http://www.metacritic.com/
movie/the-blue-room', 'title': u'The Blue Room'}, {'score': 4.0, 'link': u'http://www.metacriti
c.com/movie/the-roommate', 'title': u'The Roommate'}, {'score': 6.6, 'link': u'http://www.metac
ritic.com/movie/28-hotel-rooms', 'title': u'28 Hotel Rooms'}, {'score': 8.4, 'link': u'http://w
ww.metacritic.com/movie/the-waiting-room', 'title': u'The Waiting Room'}, {'score': 8.7, 'link'
: u'http://www.metacritic.com/movie/marvins-room', 'title': u"Marvin's Room"}, {'score': 8.4, '
link': u'http://www.metacritic.com/movie/enron-the-smartest-guys-in-the-room', 'title': u'Enron
: The Smartest Guys in the Room'}, {'score': 8.0, 'link': u'http://www.metacritic.com/movie/con
trol-room', 'title': u'Control Room'}, {'score': 7.8, 'link': u'http://www.metacritic.com/movie
/the-sons-room', 'title': u"The Son's Room"}]
```

The basic concept behind this will be that we can add any new backends we
choose to the backends directory and they will be callable from the client
object. For example:

- `client.movie.search()`
- `client.music.search()`
- `client.place.search()`
- `client.book.search()`
- `client.product.search()`
- `client.recipe.search()`

This may change a little but for now I like the way it works.
