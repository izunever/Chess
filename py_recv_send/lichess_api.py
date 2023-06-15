#!/usr/bin/env python3
import berserk
import json
import pprint
from typing import Any, Dict, Optional
pp = pprint.PrettyPrinter(indent=4)
# API_TOKEN = "lip_jzyyR1VEjZVfzhAfaSYW" # BOT TOKEN
API_TOKEN = "lip_8qGOeZUYogvePPTjKCCX" # my token pls dont steal :^)


basic_game_args = {
    "level": 2,
    "clock_limit": 600,
    "clock_increment": 10,
    "days": None,
    "color": berserk.enums.Color.WHITE,
    "variant": berserk.enums.Variant.STANDARD,
    "position": None
}

class LichessAPI:
    def __init__(self):
        self.client: berserk.Client = berserk.Client(session=berserk.TokenSession(API_TOKEN))
        # self.client.account.upgrade_to_bot() # the bot cant clean up games -> for now normal account
        self.account: Dict[str, Any] = self.client.account.get()
        self.gameId: str | None = None
        self.game = None

    def get_ongoing(self): return self.client.games.get_ongoing()
    def __clean_conn__(self): 
        [self.client.board.resign_game(game["gameId"]) for game in self.get_ongoing()]
        self.game, self.challenge, self.gameId = None, None, None

    def start_game_ai(self):
        if self.game != None:
            print("Error: the game is already being played")
        self.challenge = self.client.challenges.create_ai(**basic_game_args)
        self.gameId: str = self.challenge["id"]
        self.game = self.client.board.stream_game_state(self.gameId)

    def poll_game(self):
        ev = self.game.__next__()
        return ev
    
    def make_move(self, move: str): self.client.board.make_move(self.gameId, move)
