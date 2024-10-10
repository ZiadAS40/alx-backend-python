#!/usr/bin/env python3
"""
Given the parameters and the return values,
add type annotations to the function
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list of integers multiplied by certain factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
