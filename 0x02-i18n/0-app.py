#!/usr/bin/env python3
"""
Module that instantiates a flask instance
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """
    Returns a template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    """
    Creates the instance
    """
    app.run(host="localhost", port=3000)
