import requests
import collections

movieresult = collections.namedtuple(
    'movieresult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')


def find_movie(search):
    if not search or not search.strip():
        raise ValueError("Search text required")

    url = "http://movieservice.talkpython.fm/api/search/{}".format(search)
    resp = requests.get(url)
    resp.raise_for_status()
    movie_data = resp.json()
    movies_list = movie_data.get('hits')
    movies = [
        movieresult(**md)
        for md in movies_list
    ]
    movies.sort(key=lambda m: -m.year)
    return movies

