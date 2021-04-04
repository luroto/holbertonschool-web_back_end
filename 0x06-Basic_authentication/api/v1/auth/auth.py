#!/usr/bin/env python3
"""
Defining Auth Classes
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Class for authentication tasks
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public methor for require auth check
        """

        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        checking = 0
        for rutas in excluded_paths:
            if rutas.find(path) == -1:
                checking = -1
                break
        if checking == -1:
            return False
        if checking == 0 or checking != -1 or path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """
        Authorization header first time
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user
        """
        return None
