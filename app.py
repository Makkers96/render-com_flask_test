#pip install Flask

from flask import Flask, render_template
from main import pick_random_number

app = Flask(__name__)


@app.route("/")
def homepage():
    return "This is the homepage!"


@app.route("/html-test")
def html_test():
    number = pick_random_number()
    return render_template('html-test.html', number=number)


if __name__ == "__main__":
    app.run()