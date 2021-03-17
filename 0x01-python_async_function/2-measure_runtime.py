#!/usr/bin/env python3
"""
Measuring runtime
"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Function for measuring execution time of concurrent tasks
    """
    t0 = time.time()
    asyncio.run(wait_n(n, max_delay))
    t1 = time.time()
    fulltime = t1 - t0
    return fulltime / n
