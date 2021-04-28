#!/usr/bin/env python3
"""
Excercise file for first contact with Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Function decorator for Cache class
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Function decorator for Cache class
    """
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush("{}:inputs".format(name), str(args))
        value = method(self, *args)
        self._redis.rpush("{}:outputs".format(name), value)
        return value
    return wrapper


def replay(method: Callable) -> Callable:
    """
    Function decorator for Cache class
    """
    redis = method.__self__._redis
    name = method.__qualname__
    print("{} was called {} times:".format(name,
                                           redis.get(name).decode('utf-8')))
    inputs = redis.lrange("{}:inputs".format(name), 0, -1)
    outputs = redis.lrange("{}:outputs".format(name), 0, -1)
    full = list(zip(inputs, outputs))
    for inp, output in full:
        print("{}(*{}) -> {}".format(name, inp.decode('utf-8'),
                                     output.decode('utf-8')))


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

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
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
