#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display an hbnb template"""
    
