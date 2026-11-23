import os
import json 
# import json_stream
import yaml
import Card
import Deck
import Player

class Game(): 
    def __init__(self, game_file:str|None, players:dict|None, number_of_cpu:int|None, *args): 
        if game_file: 
            # 3. Deserialize back into Book objects using JsonMixin.from_dict()
            with open(str(chosen_game), "r", encoding="utf-8") as f:
                self._game_yaml = yaml.load(chosen_game)

                self.name = self._game_yaml["game_metadata"]["name"]

                # Handles games with one dealer
                dealer = self._game_yaml["game_config"]["dealer"]
                if dealer["dealer_enabled"]: 
                    import Dealer
                    self._dealer = Dealer(dealer)
                
                # Sets player details
                self.set_players(players)

                # Runs the base deck constructor
                self.deck_constructor()

    def set_players(self, players): 
        # Already defined in the gamepicker # Check that player array is valid and within the player_range
        # self.player_range = self._game_yaml["player"]["player_range"]
        # if len(dict(players)) not in range(self.player_range): 
        #     raise ValueError("You have too many players")
        self.players = {}
        for p in players: 
            # Need to check if this is the right syntax
            self.players.update(Player(p))

        return self._player_list
        
    def deck_constructor(): 
        self._base_deck = Deck()
        for card in self._game_yaml["deck_constructor"]["card_array"]: 
            # How do I get the append 
            self._base_deck.append(card)

    def pile_constructor(self, piles): 
    
    def hand_constructor




    def list_players(self): 
        return self._player_list
        
    def new_game_session(self): 

        if self._end_condition = 
        self.new_round()
        

    def new_round(self): 
        # for ACTIVE player?
        for player in self.active_player_list: 
            self.distribute_cards()
            for player in self.active_player_list: 
                player.take_turn()
    

    def distribute_cards(self): 

        
        
    def write_statistics(self): 
        if os.


