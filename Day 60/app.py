from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/login', methods=['GET'])
def receive_data():
    name = request.form.get("username")
    password = request.form.get("pass")
    return f"<h1>Name: {name}, Password: {password}</h1>"
    # return render_template("login.html", name=username, password=password)


if __name__ == '__main__':
    app.run()
