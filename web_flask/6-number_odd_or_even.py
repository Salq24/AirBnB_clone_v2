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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Pweb(text="is cool"):
    return ("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def isnum(n):
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def ishtml(n=None):
    if isinstance(n, int):
        return (render_template("5-number.html", n=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n=None):
    if isinstance(n, int):
        if n / 2 == 0:
            eo = "even"
        else:
            eo = "odd"
        return (render_template("6-number_odd_or_even.html", n=n, eo=eo))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)