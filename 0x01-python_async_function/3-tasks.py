#!/usr/bin/env python3
"""
Creating tasks
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Returns a Task object
    """
    running = asyncio.get_event_loop()
    return running.create_task(wait_random(max_delay))
