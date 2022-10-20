from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/blog')
def my_blogs():
    post_obj = Post()
    return render_template("index.html", posts=post_obj.all_post)


@app.route('/post/<int:blog_id>')
def my_post(blog_id):
    # print(blog_id)
    post_obj = Post()
    return render_template("post.html", id=blog_id, posts=post_obj.all_post)


if __name__ == "__main__":
    app.run(debug=True)
