#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, g, request, render_template
from flask_cors import (CORS, cross_origin)
from flask_babel import Babel


class Config(object):
    """
    Configuration class for Babel
    """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'])
def firstRoute():
    """
    First route to be implemented
    """
    return render_template('0-index.html')


@babel.localeselector
def get_locale():
    """
    Function fot get locale from request
    """
    user = getattr(g, 'user', None)
    return request.accept_languages.best_match(Config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
