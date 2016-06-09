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
