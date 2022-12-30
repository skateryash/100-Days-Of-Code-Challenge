import requests
from bs4 import BeautifulSoup

URL = "https://www.imdb.com/list/ls051594496/"

response = requests.get(URL)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movie_header = soup.find_all(name="h3", class_="lister-item-header")

list_of_top_100_movies = []

for movie in movie_header:
    movie_index = movie.find(name="span", class_="lister-item-index unbold text-primary").getText()
    movie_title = movie.find(name="a").getText()
    list_of_top_100_movies.append(movie_index + " " + movie_title)


with open("bollywood movies.txt", encoding="utf8", mode="w") as file:
    for movie in list_of_top_100_movies:
        file.write(movie + "\n")

print(list_of_top_100_movies)
print("List Scrapped successfully")
