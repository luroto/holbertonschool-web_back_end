#!/usr/bin/env python3
"""
Exploring async comprehension
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Async comprehension using an async generator
    """
    all_num = [i async for i in async_generator()]
    return all_num
