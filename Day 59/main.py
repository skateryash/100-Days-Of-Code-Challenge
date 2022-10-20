from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    post_obj = Post()
    return render_template("index.html", posts=post_obj.blog_data)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    post_obj = Post()
    return render_template("post.html", id=blog_id, posts=post_obj.blog_data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
