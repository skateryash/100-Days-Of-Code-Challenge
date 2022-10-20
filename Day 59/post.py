import requests


class Post:
    def __init__(self):
        self.blog_url = "https://api.npoint.io/15b57129a69e45911fd5"
        self.blog_response = requests.get(self.blog_url)
        self.blog_data = self.blog_response.json()
