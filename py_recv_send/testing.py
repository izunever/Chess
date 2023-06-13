from chess_board import *
from receiver import *
from test_data import inp_groups

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

sim()
        
        
        
