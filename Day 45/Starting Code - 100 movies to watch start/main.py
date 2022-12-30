import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")

list_of_top_100_movies = [movie.getText() for movie in reversed(movie_titles)]

# i = 1
# for movie in movie_titles:
#     if i != 89:
#         title = movie.getText().split(")")[1]
#     else:
#         title = movie.getText().split(":")[1]
#     list_of_top_100_movies.append(str(i) + ")" + title)
#     i = i + 1

with open("movies.txt", encoding="utf8", mode="w") as file:
    for movie in list_of_top_100_movies:
        file.write(movie + "\n")

print("List Scrapped successfully")
