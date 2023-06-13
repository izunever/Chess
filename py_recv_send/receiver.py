import chess
from typing import List
import enum
# or work with hardware

def maskstart() -> List[List[bool]]:
    return [
        [True for _ in range(8)],
        [True for _ in range(8)],
        [False for _ in range(8)],
        [False for _ in range(8)],
        [False for _ in range(8)],
        [False for _ in range(8)],
        [True for _ in range(8)],
        [True for _ in range(8)],
    ]
print(maskstart())

def map_cols(idx): return "abcdefgh"[idx]

class RecieverState(enum.Enum):
    First = 0
    Second = 1
    Third = 2

class InputProvider():
    def __init__(self):
        self.state = RecieverState.First
        self.mask1 = maskstart
        self.mask2 = None
        self.part1 = ""
        self.part2 = ""
        self.move: str | None = None

    def receive_move(self, move: List[List[bool]] | None):
        if move == None:
            return
        self.mask2 = move
        self.compute_state()
        self.mask1 = self.mask2

    def compute_state(self):
        if self.mask1 == None or self.mask2 == None:
            return
        for i in range(8):
            for j in range(8):
                if self.mask1[i][j] != self.mask2[i][j]:
                    if self.state == RecieverState.First:
                        self.part1 = map_cols(j) + str(i)
                        self.state == RecieverState.Second

                    if self.state == RecieverState.Second:
                        self.part2 = map_cols(j) + str(i)
                        to_i = i
                        to_j = j
                        self.state = RecieverState.Third

                    if self.state == RecieverState.Third:
                        if i == to_i and j == to_j:
                            self.move = self.part1 + self.part2
                            self.state = RecieverState.First
                        raise Exception
                    
    def consume(self) -> str | None:
        if self.move:
            move = self.move
            self.move = None
            return move
        else:
            return None




        
