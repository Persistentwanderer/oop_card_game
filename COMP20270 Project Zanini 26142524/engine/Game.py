import os
import json 
# import json_stream
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import Card
import Pile
import Player


class Game(): 
    def __init__(self, game_file, players, number_of_cpu, *args): 
        if game_file: 
            # 3. Deserialize back into Book objects using JsonMixin.from_dict()
            with open(str(game_file), "r", encoding="utf-8") as f:
                self._game_yaml = yaml.load(game_file, Loader=Loader)

                print yaml.dump(self._game_yaml, default_flow_style=False)
                # self.name = self._game_yaml["game_metadata"]["name"]

                # # Handles games with one dealer
                # dealer = self._game_yaml["game_config"]["dealer"]
                # if dealer["dealer_enabled"]: 
                #     import Dealer
                #     self._dealer = Dealer(dealer)
                
                # # Sets player details
                # self.set_players(players)

                # # Runs the base deck constructor
                # deck_constructor = self._game_yaml["deck_constructor"]
                # self._base_deck = Pile.Deck(deck_constructor)

    def set_players(self, players): 
        # Already defined in the gamepicker # Check that player array is valid and within the player_range
        # self.player_range = self._game_yaml["player"]["player_range"]
        # if len(dict(players)) not in range(self.player_range): 
        #     raise ValueError("You have too many players")
        self.players = {}
        for p in players: 
            # Need to check if this is the right syntax
            self.players.update(Player(p))

        return self.players
        
    # need to add legal_cards and other elements 
    def deck_constructor(card_array):
        Pile.Deck(card_array, true)

        

    # def pile_constructor(self, piles): 
    
    # def hand_constructor




    def list_players(self): 
        return self._player_list
        
    # def new_game_session(self): 
    #     if self._end_condition in implemented_end_conditions
    #     self.new_round()
        

    def new_round(self): 
        # for ACTIVE player?
        for player in self.active_player_list: 
            self.distribute_cards()
            for player in self.active_player_list: 
                player.take_turn()
    

    # def distribute_card(self, ):
            

    # def write_statistics(self): 
    #     if os.


