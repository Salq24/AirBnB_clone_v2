#!/usr/bin/python3
"""starts a web flask app"""


from models.state import State
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(self):
    """del current sql session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """displays states created"""
    states = storage.all(State)
    return render_template('9-state.html', states=states, mode="all")


@app.route('/states/<id>', strict_slashes=False)
def state_id():
    """displays states by id"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
        return render_template('9-states.html', states=state, mode='none')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
