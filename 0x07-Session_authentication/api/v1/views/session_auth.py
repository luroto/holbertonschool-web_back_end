#!/usr/bin/env python3
""" Module of session authviews
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/logout',
                 methods=['POST'], strict_slashes=False)
def all_routes() -> str:
    """ POST /api/v1/auth_session/login
    for handling session_auth routes
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if not password or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    usuario = User()
    busqueda = usuario.search({'email': email})
    if len(busqueda) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    if busqueda[0].is_valid_password(password) is False:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    return busqueda[0].to_json()


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
"""
Route for removing sessions
"""
def logout():
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
