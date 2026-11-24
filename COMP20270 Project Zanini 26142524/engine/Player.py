import Game
import Strategy
import Pile
import Card

class Player(): 
    def __init__(self, game, player_number, name, hand_config, strategy="random", cpu=True):
        self._player_number = player_number
        self._name = name 
        self.game = game 
        if cpu: 
            self.__strategy = strategy

        self.hand = []
        # Futurecasting
        # self._hands = {}
        # if hand_config: 
        #     for hand in hand_config: 
        #         self._hands.update(hand)

        self._seen_cards = []

    def add_card_to_hand(self, card): 
        if card not in self.hand: 
            self.hand.append(card)
    
    def remove_card_from_hand(self, card): 
        if card in self.hand: 
            self.hand.pop(card)

    # def take_turn(self, game_state, valid_moves): 
    #     self.strategy.chose_move(valid_moves)
        
    # # Does this need to happen at the game level? 
    # def discard(self, card, destination): 
    #     """Discards a card from the player's hand into a chose pile, taking in the card object and name of the destination pile"""
    #     discard_card = card
    #     valid_card = None
    #     for hand in self.__hands: 
    #         if card in hand:
    #             valid_card = True
    #             hand.pop(card)
    #             break
    #     if not valid_card: raise ERROR


    # def skip(): 
    #     continue

    # def draw(self, destination): 
    #     drawn_card = Pile.Deck.deal_card()
    #     destination

    # def play(self, card): 
    #     # How do I reference to the source and destination in the call in a way that I can call from in the player class
    #     self.game.play(card, self.__hand, )

    # def steal(self, source): 

    # def swap(self, source, card_to_remove): 

    def see_card(self, card:object=Card): 
        """Adds input card into the seen_card list, even if it's been seen before""" 
        self.__seen_cards.append(card)

    def __str__(self): 
        retstr = f"{self._player_number}:\tName: {self._name}"

class Greedy(Player): 
    def __init__(): 
        super().__init__()
        self.__strategy = "Greedy"

    def choose_move(self, game_state, valid_moves): 
        if "play" in valid_moves:
            # This needs to actually check the hands and will need some kind of viewable validation at some point
            largest_card = None
            for hand in self._hands:
                max(hand)
                # return the highest card 
                
            
            return
        else: return()
    # def choose_move(game_state, valid_moves): 

class Random(Player): 
    def choose_move(game_state, valid_moves): 
        return Random.choice(valid_moves)
    
    def chose_card_from_hand(self): 
        return Random.choice(self.hand)
        # if hand_type == "hand":
        #     return Random.choice(hand)




# class Tactical(Player): 
