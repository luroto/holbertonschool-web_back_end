#!/usr/bin/env python3
"""
Excercise file for first contact with Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable


class Cache():
    """
    Class for explorating cache possibilities with Redis
    """
    def __init__(self):
        """
        Constructor for Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> Union[str, bytes, int, float]:
        """
        Method that takes an argument and returns
        a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """
        Method that gets a key from REDIS
        """
        lookFor = self._redis.get(key)
        if fn:
            return fn(lookFor)
        return lookFor

    def get_str(self, key) -> str:
        """
        Method that converts from bytes to string
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key) -> int:
        """
        Method that converts from bytes to integer
        """
        value = self._redis.get(key)
        return int.from_bytes(data, sys.byteorder)
