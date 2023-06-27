#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route handle for root URL"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """Route handle for /hbnb URL"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello(text):
    """Route handle for /c/<text>URL"""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0000000', port=5000)