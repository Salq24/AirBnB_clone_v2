#!/usr/bin/python3
"""starts a web flask app"""


from models.state import State
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filter_hbnb():
    """displays states created"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states
                           , amenities=amenities)


@app.teardown_appcontext
def tearDown(exception):
    """del current sql session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
