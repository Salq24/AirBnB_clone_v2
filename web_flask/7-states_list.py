#!/usr/bin/python3
"""starts a web flask app"""


from models.state import State
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """displays states created"""
    states = storage.all()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearDown(self):
    """del current sql session"""
    storage.close()