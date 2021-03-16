#!/usr/bin/env python3
"""
Exploring duck typing
"""
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annoted version of element_length function
    """
    return [(i, len(i)) for i in lst]
