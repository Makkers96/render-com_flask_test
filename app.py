#pip install Flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return "This is the homepage!"


@app.route("/html-test")
def html_test():
    return render_template('html-test.html')


if __name__ == "__main__":
    app.run()