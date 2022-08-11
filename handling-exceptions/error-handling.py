from pydoc import describe
from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog, NotFoundException, UnauthorizedException

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/blogs")
def all_blogs():
    return jsonify(fetch_blogs())


@app.route("/blogs/<id>")
def get_blog(id: str):
    try:
        return jsonify(fetch_blog(id))
    except NotFoundException:
        return abort(404, description="Resource not found.")
    except UnauthorizedException:
        return abort(403, description="Access denied.")


app.run()
