import json
import yaml
import os

class GamePicker:
    def __init__(self): 
        self._games= {}
        self._games_directory = os.fsencode(str("./"))
        find_games(self._games_directory)

    def find_games(self): 
        for dir in os.listdir(self._games_directory):
            for file in os.listdir(dir):
                filename = os.fsdecode(file)
                if filename.endswith(".yaml"): # or filename.endswith(".yaml") or filename.endswith(".toml"): 
                    game_file = os.path.join(directory, filename)
                    game = yaml.load(game_file)
                    if game_name in self._games: 
                        # Need to figure out which error / how to prompt user for replacement : 
                        duplicate_game = input(f"There is already a game called {game_name} loaded into the game.\nDo you wish to replace it?\nY/N")

                    if not duplicate_game or duplicate_game.lower() == "y": 
                        game_name = game["game_metadata"]["name"]
                        game_art = game["game_metadata"]["cover_art"]
                        game_player_array = game["game_config"]["player_config"]["player_range"]
                        game_config = game["game_config"]
                        games.update({"name": game_name, "game_art": game_art, "game_file":game_file, "game_config": game_config})

    def change_directory(self, new_dir=None): 
        if not isinstance(new_dir,str): raise TypeError("You must enter a string")
        if not new_dir: raise ValueError("You cannot enter an empty directory when setting a new directory.")
        # need to find a way to make sure it's a valid directory
        self._games_directory = os.fsencode(str("new_dir"))

        find_games(self._games_directory)
        
    def set_players(self): 
        self.players = dict
        player_count_input = int(input("Enter the amount of players you want to play: "))
        if player_count_input not in range(self.game_player_array): 
            return ValueError("The number you entered isn't in the game's player array. ")
        for i in range(self.player_count_input+1):
            player_strategy = str(input("Enter the strategy you want to select: Tactical, Greedy, Random"))
            self.players.update({i: player_strategy.lower()})

    def start_game(self, chosen_game): 
        # Instanciates the current game by sending in a JSON file. 
        self._current_game = Game(chosen_game)