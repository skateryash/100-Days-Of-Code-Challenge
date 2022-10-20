import requests


class Post:
    def __init__(self):
        self.blogs_url = "https://api.npoint.io/b48a3d10e7da9b18541a"
        self.blog_response = requests.get(self.blogs_url)
        self.all_post = self.blog_response.json()

