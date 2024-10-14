#!/usr/bin/env python3
"""
a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay)
"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns total_time / n. Your function should return a float.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
