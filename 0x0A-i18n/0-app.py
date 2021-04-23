#!/usr/bin/env python3
"""
Route module for the API
"""

from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def firstRoute():
    """
    First route to be implemented
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
