from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "Hello There 👋"


@app.route('/guess/<username>')
def name(username):
    # parameter = {"name": "Yash"}
    # gender_response = requests.get("https://api.genderize.io", params=parameter).json()
    # age_response = requests.get("https://api.agify.io", params=parameter).json()
    # return render_template("index.html", name=username, gender=gender_response["gender"], age=age_response["age"])

    gender_response = requests.get(f"https://api.genderize.io?name={username}").json()
    age_response = requests.get(f"https://api.agify.io?name={username}").json()
    return render_template("index.html", name=username, gender=gender_response["gender"], age=age_response["age"])


@app.route('/blog')
def blogs():
    blogs_url = "https://api.npoint.io/b48a3d10e7da9b18541a"
    blog_response = requests.get(blogs_url)
    all_post = blog_response.json()
    return render_template("blogs.html", posts=all_post)


if __name__ == '__main__':
    app.run()
