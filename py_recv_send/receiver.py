import chess
from typing import List, Tuple
import enum
from common import *
# or work with hardware

def map_cols(idx): return "abcdefgh"[idx]
def map_tuples(t1: Tuple[int, int], t2: Tuple[int, int]) -> str: 
    return map_cols(7 - t1[1]) + str(8 - t1[0]) +  map_cols(7 - t2[1]) + str(8 - t2[0])

class RecieverState(enum.Enum):
    MoveOwnerPiece = 0
    TargetSquare = 1
    Capture = 2
    Done = 3

class InputProvider():
    def __init__(self, init_mask=maskstart()):
        self.state = RecieverState.MoveOwnerPiece
        self.curr_mask = init_mask # stan maski ktora jest teraz
        self.recv_mask = None # maska otrzymywana
        self.origin: Tuple[int, int] | None = (0, 0)
        self.target: Tuple[int, int] | None = (0, 0)
        self.move: str | None = None

    def receive_mask(self, mask_received: List[List[bool]] | None):
        if mask_received == None:
            return
        self.recv_mask = mask_received
        self.compute_state()
        self.curr_mask = self.recv_mask

    def compute_state(self):
        if self.curr_mask == None or self.recv_mask == None:
            return
        for i in range(8):
            for j in range(8):
                if self.curr_mask[i][j] != self.recv_mask[i][j]:
                    match self.state:
                        case RecieverState.MoveOwnerPiece:
                            self.origin = (i, j)
                            self.state = RecieverState.TargetSquare
                        case RecieverState.TargetSquare:
                            if self.curr_mask[i][j] - self.recv_mask[i][j] == 1:
                                self.target = (i, j)
                                self.state = RecieverState.Capture
                            else:
                                self.target = (i, j)
                                self.move = map_tuples(self.origin, self.target)
                                self.state = RecieverState.Done
                                self.origin, self.target = None, None
                        case RecieverState.Capture:
                            if i == self.target[0] and j == self.target[1]:
                                self.move = map_tuples(self.origin, self.target)
                                self.state = RecieverState.Done
                                self.origin, self.target = None, None                    
                    
    def consume(self) -> str | None:
        if self.state == RecieverState.Done:
            move = self.move
            self.move = None
            self.state = RecieverState.MoveOwnerPiece
            return move
        else:
            return None
