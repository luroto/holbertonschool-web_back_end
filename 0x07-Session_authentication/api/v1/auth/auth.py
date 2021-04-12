#!/usr/bin/env python3
"""
Defining Auth Classes
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """
    Class for authentication tasks
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method for require auth check
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] == '/':
            path = path[:-1]
        for rutas in excluded_paths:
            if path in rutas:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header first time
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a Cookie value from a request
        """
        if request is None:
            return None
        cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
