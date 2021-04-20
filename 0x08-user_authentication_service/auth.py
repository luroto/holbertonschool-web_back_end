#!/usr/bin/env python3
"""
Auth functions
"""
import bcrypt
from db import DB
from user import User
import uuid


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if an existing email matches with provided password
        """
        user = self._db.find_user_by(email)
        if user.email == email:
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        return False

    def _generate_uuid(self):
        """
        Returns a string rep of a UUID
        """
        return str(uuid.UUID)
