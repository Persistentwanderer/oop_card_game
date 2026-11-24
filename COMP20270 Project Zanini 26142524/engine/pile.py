import Card
# import ABC

class Pile():
    def __init__(self, visibility):
        self.__card_list = []

    def deal_card(self, destination): 
        # check the instance / class of the source and the destination
        # then
        card_to_deal = self.__card_list[0]
        self.__card_list.pop[0]
        return card_to_deal
        
    # def add_card_to_deck(self, card): 
    #     """Appends a card object to the pile"""
    #     self.__card_list.append(card)

    def shuffle(self):
        """Shuffles the pile"""
        random.shuffle(self.__card_list)
        return

    def return_pile(self): 
        """Returns a copy of the card list array."""
        if self._visibility == 1: 
            return self.__card_list.copy()
        else: return None
    
    def return_pile_sorted_by_attribute(self, attribute): 
        self.__pile_sorted_by_attribute = []
        for c in self.__card_list: 
            self.__pile_sorted_by_attribute.add(c.get_attributes())

        return sorted(self.__deck_sorted_by_attribute, key=lambda x: x[attribute])
        # reverse the string to make it so that the suit is the first thing that is ranked

    def __setitem__(self, card):
        self.__card_list.append(card)

    # def __getitem__(self): 


    def __str__(self): 
        if self.visible == True: 
            output = ""
            for card in self.__card_list: 
                output+=str(card)+" "
            return output
        else: return None


class DrawPile(Pile): 
    def __init__(self, card_array, visibility=False):
        super().__init__(card_array, visibility)
        


# class DiscardPile(Pile): 
#     def __init__(self, cards):
#         super().__init__()


# class PlayPile(Pile):
#     def __init__(self, cards):
#         super().__init__()

# class Hand(Pile): 
#     def __init__(self, player):
#         super().__init__()

class Deck(Pile):
    def __init__(self, card_array, visibility):
        super().__init__(visibility)
        for c in card_array:
            c_value = c[0]
            c_suit = c[1]
            self.__card_list.append(Card.Card(c_value, c_suit))
        self.visible = visibility
    

    def __setitem__(): 
        return ValueError("Cannot add a card to the main deck after init")