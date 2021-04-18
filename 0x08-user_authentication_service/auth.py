#!/usr/bin/env python3
"""
Auth functions
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password):
    """
    Method that takes in password strings and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        creates an user object based on email and password
        """
        if self._db.find_user_by(email=email) is not None:
            raise ValueError("{} already exists".format(email))
        passi = _hash_password(password)
        return self._db.add_user(email, passi)
