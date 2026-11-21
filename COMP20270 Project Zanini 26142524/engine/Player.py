import Game
import Strategy
import Pile

class Player(): 
    def __init__(self, player_number, name, strategy="random", *kwargs):
        self._player_number = player_number
        self._name = name 
        self.__strategy = strategy
        if piles: 
            for pile in piles: 
                self.__"pile" = pile

    def take_turn(self, game_state, valid_moves): 

        self.strategy.chose_move(valid_moves)
        
    def discard(self, source, destination): 
        source

    def skip(): 
        continue

    def draw(self,source, destination): 
        destination

    def play(self, source, destination): 

        for card in murder 

    def __str__(self): 
        retstr = f"{self._player_number}:\tName: {self._name}"