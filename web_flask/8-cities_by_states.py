#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
@app.route("cities_by_states", strict_slashes=False)
def cities_by_states():
    """Returns a list of cities by states."""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)