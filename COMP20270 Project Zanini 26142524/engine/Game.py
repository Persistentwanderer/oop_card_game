import os
import json 
import json_stream
import card
import deck

class Game(): 
    def __init__(self, game_file=None, players=None, number_of_cpu=None): 
        if game_file: 
            # 3. Deserialize back into Book objects using JsonMixin.from_dict()
            with open(str(chosen_game), "r", encoding="utf-8") as f:
                self.__base = json-load.load(chosen_game)

                self.name = self.__base["name"]

                # Handles games with one dealer
                if dealer: 
                    import Dealer
                    self.dealer = Dealer(attributes)
                
                # Sets player details
                self.set_players(players)

                # Deck constructor
                self.set_base_deck()

                # 

    def set_players(self): 
        # Check that player array is valid and within the player_range
        self.player_range = self.__base["player"]["player_range"]
        if len(dict(players)) not in range(self.player_range): 
            raise ValueError("You have too many players")
        self.players = {}
        for p in players: 
            # Need to check if this is the right syntax
            self.players.update(p)
        


        return self._player_list


    def return_players(self, players): 
        



    
    
    def new_game_session(self): 
        self.

    def new_round(self)        
        # for ACTIVE player?
        for player in self.active_player_list: 
            self.distribute_cards()
            for player in self.active_player_list: 
                player.take_turn()
    

    def distribute_cards(self): 

        
        
    def write_statistics(self): 
        if os.


