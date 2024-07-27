#!/usr/bin/python3
""" starts a Flask web application. """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays Hello Hbnb>"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays HBNB."""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays C followed by the value of the text variabl."""

    replace_underscore = text.replace('_', ' ')
    return f"C {replace_underscore}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
