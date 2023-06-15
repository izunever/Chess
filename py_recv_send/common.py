#!/usr/bin/env python3
from typing import List, Tuple

def maskstart() -> List[List[bool]]:
    return [
        [1 for _ in range(8)],
        [1 for _ in range(8)],
        [0 for _ in range(8)],
        [0 for _ in range(8)],
        [0 for _ in range(8)],
        [0 for _ in range(8)],
        [1 for _ in range(8)],
        [1 for _ in range(8)],
    ]

def map_cols(idx): return "abcdefgh"[idx]
def map_tuples(t1: Tuple[int, int], t2: Tuple[int, int]) -> str: 
    return map_cols(7 - t1[1]) + str(8 - t1[0]) +  map_cols(7 - t2[1]) + str(8 - t2[0])
