#!/usr/bin/python3
""" flask script """

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """function for web app route"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """function for hbnb route"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """displays value of /c/<text> web app route"""
    text = text.replace("_", " ")
    return "C %s" % text

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """displays value of /python/<text> web app route"""
    text = text.replace("_", " ")
    return "Python %s" % text

@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """displays n if n is a number web app route"""
    return "%d is a number" % n

@app.route("/number_template/<int:n>", strict_slashes=False)
def numtemplate_route(n):
    """renders n int template file if n is a number, web app route"""
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_route(n):
    """renders odd or even in template file if n is a number, web app route"""
    if n % 2 == 0:
        oe = 'even'
    else:
        oe = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, oe=oe)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
