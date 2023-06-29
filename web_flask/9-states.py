#!/usr/bin/python3
"""Script to start a Flask web application"""
from flask import Flask
from models import storage
from models.state import State
from flask import jsonify


app = Flask(__name__)

@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Session"""
    storage.close()
    
@app.route('/states', strict_slashes=False)
def states():
    """Returns a list of all states"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])

@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Returns a specific state"""
    state = storage.get(State, id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(state.to_dict())