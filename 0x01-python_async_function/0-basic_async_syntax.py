#!/usr/bin/env python3
"""
First asyncio task
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument that
    waits for a random delay between 0 and max_delay returning it
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
