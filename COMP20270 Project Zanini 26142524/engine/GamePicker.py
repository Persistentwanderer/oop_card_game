import json
import os

class GamePicker:
    def __init__(self): 
        self._games= {}
        self._games_directory = os.fsencode(str("./"))
        find_games(self._games_directory)
        # for game in self._games: 
            # code to access this directory in the API

    def find_games(self): 
        for file in os.listdir(self._games_directory):
            filename = os.fsdecode(file)
            if filename.endswith(".json"): # or filename.endswith(".yaml") or filename.endswith(".toml"): 
                game_file = os.path.join(directory, filename)
                game = json.load(game_file)
                game_name = game["name"]
                game_art = game["cover_art"]
                if game_name in self._games: 
                    # Need to figure out which error / how to prompt user for replacement : 
                    duplicate_game = input(f"There is already a game called {game_name} loaded into the game.\nDo you wish to replace it?\nY/N")

                if not duplicate_game or duplicate_game.lower() == "y": 
                    self._games.update({"name": game_name, "game_art": game_art, "game_file":game_file})

    def change_directory(self, new_dir=None): 
        if not isinstance(new_dir,str): raise TypeError("You must enter a string")
        if not new_dir: raise ValueError("You cannot enter an empty directory when setting a new directory.")
        # need to find a way to make sure it's a valid directory
        self._games_directory = os.fsencode(str("new_dir"))

        find_games(self._games_directory)
        

    def start_game(self, chosen_game): 
        # Instanciates the current game by sending in a JSON file. 
        self._current_game = Game(chosen_game)