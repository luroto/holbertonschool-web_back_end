#!/usr/bin/env python3
"""
Function for calculating indexes for page
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the indexes contained in a page given a page_size
    """
    return ((page - 1) * page_size, page * page_size)
