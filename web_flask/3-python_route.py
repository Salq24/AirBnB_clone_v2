#!/usr/bin/python3
"""This script starts a flask web app, listening
on 0.0.0.0, port 5000
"""


from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hbnb_hello():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cweb(text):
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python/<text>", strict_slashes=False)
dey python(text="is cool"):
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
