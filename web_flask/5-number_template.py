#!/usr/bin/python3
""" starts a Flask web application. """
from flask import Flask
from flask import render_template


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


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """display Python, followed by the value of the text variable."""

    replace_text = text.replace('_', ' ')
    return 'Python {}'.format(replace_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer."""

    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer."""

    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
