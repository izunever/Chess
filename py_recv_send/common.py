from typing import List

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