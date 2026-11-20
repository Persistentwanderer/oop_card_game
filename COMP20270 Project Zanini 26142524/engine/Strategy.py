import game
import random

class Strategy(): 
    def __init__(self): 
        self.strategies = []
    


class GreedyStrategy(Strategy): 
    def __init__(self, motivation): 
        super().__init__(self)

class RandomStrategy(Strategy): 
    def __init__(self): 
        super().__init__(self)

    def chose_card(source, destination): 
        chosen_card = random.choice(source)
        Deck.card_removesource

class TacticalStrategy(Strategy): 
    def __init__(self, motivation, players, decks): 
        super().__init__(self)
        self.__seen_cards = {}




