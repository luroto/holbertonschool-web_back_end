#!/usr/bin/env python3
""" For encrypt password """
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashing password
    """
    pwd = password.encode()
    hashingpw = bcrypt.hashpw(pwd, bcrypt.gensalt())

    return hashingpw


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checking if it is valid """
    valid = password.encode()
    if bcrypt.checkpw(valid, hashed_password):
        return True
    else:
        return False