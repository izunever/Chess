#!/usr/bin/env python3
from chess_board import *
from receiver import *
import pprint
from test_data import inp_groups
from lichess_api import LichessAPI
from time import sleep
import os

pp = pprint.PrettyPrinter(indent=4)

def com():
    # TODO
    pass

def sim():
    for (res, inp) in inp_groups.items():
        print(f"\nTEST: {res[0]}")
        chessboard = BlindBoard()
        print(chessboard.chessboard)
        inp_provider = InputProvider(init_mask=inp[0])
        print(inp_provider.state)
        for mask in inp:
            inp_provider.receive_mask(mask)
            probe = inp_provider.consume()
            print(inp_provider.state)
            if probe:
                print(probe)
                result = chessboard.make_move(probe)
                print(chessboard.chessboard)
            else:
                print("Move not ready")
        assert(result == res[1])

def api():
    lapi = LichessAPI()
    lapi.start_game_ai()
    chessboard = BlindBoard()
    print(chessboard.chessboard)
    while True:
        try:
            inp = input("(check / (move) / exit): ")
            if inp == "exit":
                break
            try:
                chessboard.chessboard.parse_uci(inp)
            except ValueError:
                print("The input move has to be in the uci format (ex: \"a2a3\")")
                continue
            if chessboard.make_move(inp):
                lapi.make_move(inp)
                print(chessboard.chessboard, "\n")
            else:
                print("Invalid input")
                continue
            print("Waiting for the ai move ...")
            ai_move = lapi.poll_wait(inp)
            chessboard.make_move(ai_move)
            print(chessboard.chessboard, "\n")
        except Exception as e:
            print(e)
    lapi.__clean_conn__()


if __name__ == "__main__":
    mode = os.environ.get("MODE")
    if mode == "sim":
        sim()
    elif mode == "api":
        api()
    elif mode == "clean":
        LichessAPI().__clean_conn__()
