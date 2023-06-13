#!/usr/bin/env python3
import berserk
import chess
import flask
import receiver
API_TOKEN = "lip_4EBtAZbxUPQWmizc7JOJ"


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
    
# def sim():
#     input_provider = receiver.InputProvider()
    



# session = berserk.TokenSession(API_TOKEN)
# client = berserk.Client(session=session)
# board = BlindBoard()
# print(board.make_move("a2a5"))
# print(board.chessboard)
# print(board.make_move("g7g6"))
# print(board.chessboard)
# print(board.chessboard.fen())

# hardware -> comm -> flask? z import chess -> komunikacja z api za pomoca fen