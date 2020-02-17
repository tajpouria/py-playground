from flask import Flask
import os

app = Flask(__name__)

app.config['SOME_KEY'] = os.getenv('SOME_KEY')


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About good</h1>"
