#!/usr/bin/env python3
"""
Route module for the API and handling of translations
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    Configuration class for Babel
    """
    LANGUAGES = ["en", "fr"]


def get_user():
    """
    Function for checking for user or login_as
    """
    user_id = request.args.get('login_as')
    return users.get(int(user_id))


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', methods=['GET'])
def firstRoute():
    """
    First route to be implemented
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """
    Function fot get locale from request
    """
    user_locale = request.args.get('locale')
    if user_locale is not None and user_locale in app.config['LANGUAGES']:
        return user_locale
    user_locale = get_user()
    if user_locale is not None:
        return user_locale['locale']
    user_locale = request.headers.get('locale')
    if user_locale is not None:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """
    Sets username as global variable for everything inside flask
    """
    user = get_user()
    if user is not None:
        g.user = user


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
