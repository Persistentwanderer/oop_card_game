import Game
import random
import Player

class Strategy(): 
    def __init__(self, game): 
        self.game = game       

class GreedyStrategy(Strategy): 
    def __init__(self, player, motivation): 
        super().__init__()
        self.__motivation = motivation
    def choose_move(self, valid_moves): 
        if "play" in valid_moves:
            player.play_highest_card()

class RandomStrategy(Strategy): 
    def __init__(self): 
        super().__init__()

    def choose_move(self, valid_moves): 
        return random.choice(valid_moves)


    def chose_card(source, destination): 
        chosen_card = random.choice(source)
        return 

class TacticalStrategy(Strategy): 
    def __init__(self, motivation, player, other_players, **kwargs): 
        super().__init__()
        for player in players: 
            self.__f"{player}"_seen_cards = []
        
        if 

        self.__seen_cards = {}





