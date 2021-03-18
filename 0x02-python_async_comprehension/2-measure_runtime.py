#!/usr/bin/env python3
"""
Exploring four parallel comprehensions in 10 seconds
"""

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns the time of execution of a program executed 4 times in parallel
    """
    t0 = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    t1 = time()
    return t1 - t0
