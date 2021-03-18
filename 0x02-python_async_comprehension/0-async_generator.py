#!/usr/bin/env python3
"""
Exploring async generators
"""

import asyncio
import random
from typing import Generator


async def async_generator():
    """
    Function that creates an async generator of numbers between 0 and 10
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, +10)
