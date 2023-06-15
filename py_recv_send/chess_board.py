#!/usr/bin/env python3
import chess
import receiver

class BlindBoard:
    def __init__(self, starting_fen=chess.STARTING_BOARD_FEN):
        self.chessboard = chess.Board(fen=starting_fen)
    def poke(self):
        return self.chessboard.generate_legal_moves()

    # manipulates fen state of chessboard
    def make_move(self, move) -> bool: 
        if chess.Move.from_uci(move) in self.chessboard.legal_moves:
            self.chessboard.push_uci(move)
            return True
        return False

    def is_legal(self, move: str):
        return self.chessboard()
