from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title.string)

articles = soup.find_all(class_="titleline")     #
# print(article_tag)
article_texts = []
article_links = []

for article in articles:
    text = article.find(name="a").getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

print(article_texts)
print(article_links)


upvotes = soup.find_all(class_="score")  # .getText()
article_upvotes = []
for score in upvotes:
    vote = int(score.getText().split(" ")[0])
    article_upvotes.append(vote)

print(article_upvotes)

vote_index = article_upvotes.index(max(article_upvotes))

print(article_texts[vote_index])
print(article_links[vote_index])
print(article_upvotes[vote_index])













# with open("website.html", encoding="utf8") as file:
#
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tag = soup.find_all(name="a")
# # print(all_anchor_tag)
#
# # for tag in all_anchor_tag:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# # print(section_heading.getText())
# # print(section_heading.name)
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# name = soup.select_one(selector="#name")
# # print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)
#
