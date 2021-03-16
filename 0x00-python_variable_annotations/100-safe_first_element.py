#!/usr/bin/env python3
"""
Correcting duck type annotations
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Ensuring data type of return function
    """
    if lst:
        return lst[0]
    return None
