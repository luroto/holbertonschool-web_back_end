#!/usr/bin/env python3
"""
Defining BasicAuth Classes
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Based on Auth we create the Basic Auth
    """
    def extract_base64_authorization_header(self, authorization_header: str)
    -> str:
        """
        Returns the Base64 part of the Authorization header for a basic
        Authentication
        """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is not True:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        return authorization_header[6:]
