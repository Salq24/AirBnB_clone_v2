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


@app.route('/cities_by_state', strict_slashes=False)
def list_cities():
    """displays states created"""
    states = storage.all(State)
    return render_template('8-cities_by_state.html', states=states)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
