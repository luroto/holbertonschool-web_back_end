#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from flask import Flask, jsonify, abort, request, redirect, url_for
from flask_cors import (CORS, cross_origin)
from auth import Auth
import os

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def firstRoute():
    """
    First route to be implemented
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    Route for creating users via Auth
    """
    data = request.get_data()
    data = data.decode('utf-8')
    allData = {}
    allItems = data.split('&')
    for item in allItems:
        pair = item.split('=')
        allData[pair[0]] = pair[1]
    try:
        AUTH.register_user(allData['email'], allData['password'])
        return jsonify({"email": allData['email'],
                        "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    Login function for POST/sessions route
    """
    data = request.form
    user = AUTH._db.find_user_by(email=data['email'])
    if user is None:
        abort(401)
    if AUTH.valid_login(email=user.email, password=data['password']):
        cookie = AUTH.create_session(email=user.email)
        response = jsonify({"email": user.email, "message": "logged in"})
        response.set_cookie("session_id", cookie)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    Logout function for destroying session and redirect user to get
    """
    data = request.form
    user = AUTH._db.find_user_by(data['session_id'])
    if user:
        AUTH.destroy_session(user.id)
        redirect(url_for('/'))
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """
    Returns a user profile
    """
    data = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(data)
    print("Este es user: ", user)
    if user:
        return jsonify({"email": user.email})
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
