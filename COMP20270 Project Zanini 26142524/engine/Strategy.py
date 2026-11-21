import game
import random

class Strategy(): 
    def __init__(self):         

class GreedyStrategy(Strategy): 
    def __init__(self, motivation): 
        super().__init__()
        self.__motivation = motivation
    def choose_move(self, valid_moves): 
        for 

class RandomStrategy(Strategy): 
    def __init__(self): 
        super().__init__()

    def choose_move(self, valid_moves): 
        return random.choice(valid_moves)


    def chose_card(source, destination): 
        chosen_card = random.choice(source)
        Deck.card_removesource

class TacticalStrategy(Strategy): 
    def __init__(self, motivation, players, **kwargs): 
        super().__init__()
        for player in players: 
            self.__f"{player}"_seen_cards = []
        
        if 

        self.__seen_cards = {}





