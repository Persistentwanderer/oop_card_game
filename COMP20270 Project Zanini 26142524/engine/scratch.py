import Card
import Pile
import Game
# import Player


card_list = [[1,1], [1,2], [1,4],[2,3]]
player_dict = dict({1: "Random", 2: "Random"})
c = Card.Card(1,1)
d = Pile.Deck(card_list, True)
g = Game.Game("/Users/alfie/Documents/code/oop_card_game/COMP20270 Project Zanini 26142524/games/template/template_easy.yaml", player_dict, None)

print(c)
# p = Player.Player(1,"Hello","random")

print(d)
# print(p)