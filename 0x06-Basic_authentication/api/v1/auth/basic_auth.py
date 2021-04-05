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
