
import requests
import collections

movieresult = collections.namedtuple(
    'movieresult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')
search = input("enter some movie name")
url = "http://movieservice.talkpython.fm/api/search/{}".format(search)
resp = requests.get(url)
resp.raise_for_status()
movie_data = resp.json()
movies_list = movie_data.get('hits')
print(movies_list)
# movies = []
#
# for md in movies_list:
#     m = movieresult(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         Capitalism=md.get("Capitalism"),
#         director=md.get("director"),
#         keywords=md.get("keywords"),
#         duration=md.get("duration"),
#         genres=md.get("genres"),
#         year=md.get("year")
#     )
#     movies.append(m)

# def method(x, y, z , **kwargs):
#     print(kwargs)
#
# method(1, 2, z=9, format = True, age = 7)

# It is only possible only when the title = md.get('title') title same.


movies = [
    movieresult(**md)
    for md in movies_list
]



print(f"Found {len(movies)} movies of {search}")
for m in movies:
    print(f"{m.title}--------------------{m.year}")