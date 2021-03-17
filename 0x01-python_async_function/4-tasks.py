#!/usr/bin/env python3
"""
Calling function
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Executing multiple coroutines given a first function
    """
    all_tasks = []
    all_delays = []
    delay = 0
    for _ in range(n):
        all_tasks.append(wait_random(max_delay))

    for task in all_tasks:
        all_delays.append(await(task))
    return all_delays
