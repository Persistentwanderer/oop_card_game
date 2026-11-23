import Game
import Strategy
import Pile

class Player(): 
    def __init__(self, game, player_number, name, strategy="random", cpu=True):
        self._player_number = player_number
        self._name = name 
        self.game = game 
        if cpu: 
            self.__strategy = strategy

        self.__hand = {}
        # How to call upon the game object without creating a useless link?

        # if draw_pile: 
        #     self._draw_pile = draw_pile


    def take_turn(self, game_state, valid_moves): 
        self.strategy.chose_move(valid_moves)
        
    def discard(self, source, destination): 
        source

    def skip(): 
        continue

    def draw(self, destination): 
        drawn_card = Pile.Deck.deal_card()
        destination

    def play(self, card): 
        # How do I reference to the source and destination in the call in a way that I can call from in the player class
        self.game.play(card, self.__hand, )

    def steal(self, source): 

    def swap(self, source, card_to_remove): 



    def __str__(self): 
        retstr = f"{self._player_number}:\tName: {self._name}"