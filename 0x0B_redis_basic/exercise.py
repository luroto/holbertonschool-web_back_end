#!/usr/bin/env python3
"""
Excercise file for first contact with Redis
"""
import redis
import uuid
from typing import Union


class Cache():
    """
    Class for explorating cache possibilities with Redis
    """
    def __init__(self):
        """
        Constructor for Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb(self)

    def store(self, data) -> Union[str, bytes, int, float]:
        """
        Method that takes an argument and returns
        a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
