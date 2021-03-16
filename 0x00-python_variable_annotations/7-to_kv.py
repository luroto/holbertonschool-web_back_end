#!/usr/bin/env python3
"""
Exploring the handling of different types of inputs
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of a string and a float
    """
    return (k, v ** 2)
