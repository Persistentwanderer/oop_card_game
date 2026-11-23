import Card
import ABC

class Pile(ABC):
    def __init__(self, input_cards, visibility): 
        self.__card_list = []
        for card in input_cards: 
            self.__card_list.append(Card(card))

    def deal_card(self, destination): 
        #check the instance / class of the source and the destination
        # then
        card_to_deal = self.__card_list[0]
        self.__card_list.pop[0]
        return card_to_deal
        
    def add_card_to_deck(self, source): 
        self.__card_list.append(source)

    def shuffle(self):
        self.__card_list = random.shuffle(self.__card_list)
        return self.__card_list

    def return_deck(self): 
        if self._visibility == 1: 
            return self.__card_list
        else: return None
    
    def return_pile_sorted_by_attribute(self, attribute): 
        self.__pile_sorted_by_attribute = []
        for c in self.__card_list: 
            self.__pile_sorted_by_attribute.add(c.get_attributes())

        return sorted(self.__deck_sorted_by_attribute, key=lambda x: x[attribute])
        # reverse the string to make it so that the suit is the first thing that is ranked

    def __setitem__(self, card):
        self.__card_list.append(card)

    def __str__(self): 
        return self.__card_list


class DrawPile(Pile): 
    def __init__(self, cards):
        super().__init__()


class DiscardPile(Pile): 
    def __init__(self, cards):
        super().__init__()


class PlayPile(Pile):
    def __init__(self, cards):
        super().__init__()

class Hand(Pile): 
    def __init__(self, player):
        super().__init__()

class Deck(Pile):
    def __init__(self, card_list):
        super().__init__()
        for card in card_list: 
            self._
