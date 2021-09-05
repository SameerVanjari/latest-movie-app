import requests
from bs4 import BeautifulSoup

URL = 'https://www.hungama.com/movies/hindi/'

def get_movies():
    req = requests.get(URL)
    soup = BeautifulSoup(req.content, 'html5lib')

    movies =[]

    table = soup.find('div', attrs={'id':'blockmovies'})

    for row in table.find_all('div', attrs={'class': 'movie-img'}):
        movie = {}
        movie['url'] = row.a['href']
        movie['image'] = row.img['src']
        movie['title'] = row.a['title']
        movies.append(movie)
    
    return movies
