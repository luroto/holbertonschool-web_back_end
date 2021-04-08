#!/usr/bin/env python3
"""
Defining BasicAuth Classes
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """
    Based on Auth we create the Basic Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is not True:
            return None
        try:
            decod = base64.b64decode(
                    base64_authorization_header.encode('utf-8'))
            return decod.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
                                self,
                                decoded_base64_authorization_header: str
                                ) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if isinstance(decoded_base64_authorization_header, str) is not True:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        contents = decoded_base64_authorization_header.split(":")
        return (contents[0], contents[1])

    def user_object_from_credentials(
                                    self,
                                    user_email: str,
                                    user_pwd: str
                                    ) -> TypeVar('User'):
        """
        Returns a User instance based on email & password
        """
        if user_email is None or isinstance(user_email, str) is not True:
            return None
        if user_pwd is None or isinstance(user_pwd, str) is not True:
            return None
        try:
            busqueda = User.search({'email': user_email})
            for usuario in busqueda:
                if usuario.is_valid_password(user_pwd) is True:
                    return usuario
        except Exception:
            return None
