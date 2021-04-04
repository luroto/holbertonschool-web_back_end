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
        ruti = ""
        pathos = ""
        for rutas in excluded_paths:
            if rutas.find(path) == -1:
                if path[-1] == '/':
                    ruti = path[:-1]
                else:
                    ruti = path
                if rutas[-1] == '/':
                    pathos = rutas[:-1]
                else:
                    pathos = rutas
                if len(pathos) == len(ruti):
                    for i in range(len(ruti)):
                        if pathos[i] != ruti[i]:
                            return True
                return False
        if path in excluded_paths:
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
