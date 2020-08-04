import requests
from bs4 import BeautifulSoup
import re

URL = "https://movie.naver.com/movie/running/current.nhn"


response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

movie = soup.select('#content > .article > .obj_section >.lst_wrap > ul > li')

#print(soup)
#print(movie)

content = []

for m in movie :
    movie_dict = {}
    a_tag = m.select_one('dl > dt > a')

    movie_link = a_tag['href']
    movie_title=a_tag.getText()
    movie_href = movie_link.split('=')[1]

    # print(movie_link)
    # print(movie_title)
    # print(movie_href)
    
    movie_data = {
        'title' : movie_title,
        'link' : movie_href
    }

    content.append(movie_data)

print(content)