from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underline
def bye():
    return "<u><em><b>Bye!</b></em></u>"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."


if __name__ == '__main__':
    app.run(debug=True)
