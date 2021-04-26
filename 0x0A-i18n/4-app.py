#!/usr/bin/env python3
"""
Route module for the API incluiding getlocale function based
on query parameters
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext


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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Function fot get locale from request
    """
    user_locale = request.args.get('locale')
    if user_locale is not None and user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
