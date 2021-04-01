#!/usr/bin/env python3
"""
Defining Auth Classes
"""
from flask import request
from typing import List


class Auth():
    """
    Class for authentication tasks
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public methor for require auth check
        """
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
