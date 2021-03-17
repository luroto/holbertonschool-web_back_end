#!/usr/bin/env python3
"""
First asyncio task
"""
import asyncio

async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that takes in an integer argument that
    waits for a random delay between 0 and max_delay returning it
    """
    await asyncio.sleep(max_delay)
    return 