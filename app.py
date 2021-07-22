import os

import flask

app = flask.Flask(__name__)


@app.route("/")
def hello():
    return "Hello world from Shipa!"

app.run(port=5000, host="0.0.0.0")
