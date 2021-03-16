#!/usr/bin/env python3
"""
Exploring complex types
"""
from typing import List

InputList = List[float]


def sum_list(input_list: InputList) -> float:
    """
    Returns a sum of list of floats
    """
    return sum(input_list)
