#!/usr/bin/env python3
"""
Exploring mix of multiple types
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of mixed ints and floats
    """
    return sum(mxd_lst)
