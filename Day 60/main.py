from flask import Flask, render_template, request
from post import Post
import smtplib

app = Flask(__name__)
MY_EMAIL = "mrfrek78@gmail.com"
# OWNER_EMAIL = "ygcjal@gmail.com"
MY_PASSWORD = "klspryxyxahzfsna"


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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form.get("email"))
        print(request.form.get("phone"))
        print(request.form.get("message"))
        # name = request.form.get("name")
        # email = request.form.get("email")
        # phone = request.form.get("phone")
        # message = request.form.get("message")
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(MY_EMAIL, MY_PASSWORD)
        #     connection.sendmail(
        #         from_addr=MY_EMAIL,
        #         to_addrs=MY_EMAIL,
        #         msg=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage= {message}"
        #     )
        success = "Successfully sent your message"
        return render_template("contact.html", message=success)
    return render_template("contact.html", message="Contact Me")


# @app.route('/form-entry', methods=["GET", "POST"])
# def receive_data():
#     print(request.form.get("name"))
#     print(request.form.get("email"))
#     print(request.form.get("phone"))
#     print(request.form.get("message"))
#     return "<h1>Successfully sent your message</h1>"


if __name__ == '__main__':
    app.run(debug=True)
