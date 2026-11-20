import os
import json 
import json_stream
import Card
import Deck

class Game(): 
    def __init__(self, game_file=None, player=None, cpu_player=None): 
        if game_file: 
            # 3. Deserialize back into Book objects using JsonMixin.from_dict()
            with open(str(chosen_game), "r", encoding="utf-8") as f:
                self.__base = json-load.load(chosen_game)

                self.name = self.__base["name"]

                self.player_range = self.__base["player"]["player_range"]

                self.players = dict(self.set_players(self.__base["players"]))

                self.__opening_hand_size = self.__base()

    @property
    def players(self): 
        return self._player_list

    @setter
    def players(self, players): 
        if len(players) in range(self.player_range): 


    
    def new_match(self): 
        for player in self._player_list: 
            self.distribute_cards()
    

    def distribute_cards(self, player): 

        
        
    def write_statistics(self): 
        if os.



                