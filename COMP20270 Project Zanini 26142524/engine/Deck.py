import random

class Deck():
    def __init__(self, input_cards, limits): 
        self.__card_list = []
        for card in input_cards: 
            self.__card_list.append(Card(card))

    def deal_card(self, source, destination): 
        #check the instance / class of the source and the destination
        # then 
        
        
    def deck_shuffle(self):
        self.__card_list = random.shuffle(self.__card_list)
        return self.__card_list
