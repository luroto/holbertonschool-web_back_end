#!/usr/bin/env python3
"""
Auth functions
"""
import bcrypt


def _hash_password(password):
    """
    Method that takes in password strings and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
