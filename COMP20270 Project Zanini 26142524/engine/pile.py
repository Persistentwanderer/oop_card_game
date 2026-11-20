import Card

class Pile():
    def __init__(self, input_cards, visibility): 
        self.__card_list = []
        for card in input_cards: 
            self.__card_list.append(Card(card))

    def deal_card(self, source, destination): 
        #check the instance / class of the source and the destination
        # then
        card_to_deal = self.__card_list[0]
        self.__card_list.pop[0]
        return card_to_deal
        
    def shuffle(self):
        self.__card_list = random.shuffle(self.__card_list)
        return self.__card_list


    # def sorted_remaining_view(self): 
    #     if self.visibility == 1: 
    #         return sorted(self.__input_cards)
    #     else: return None
    
    def print_deck(self): 
        if self._visibility == 1: 
            return self.__card_list
        else: return None


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
    def __init__(self):
        super().__init__()

    def __init__(self, input_cards, visibility): 
        self.__card_list = []
        for card in input_cards: 
            self.__card_list.append(Card(card))

    def deal_card(self, source, destination): 
        #check the instance / class of the source and the destination
        # then
        card_to_deal = self.__card_list[0]
        self.__card_list.pop[0]
        return card_to_deal
        
    def shuffle(self):
        self.__card_list = random.shuffle(self.__card_list)
        return self.__card_list


    def view_initial_deck(self): 
        full_deck

    def sorted_remaining_view(self): 
        if self.visibility == 1: 
            return sorted(self.__input_cards)
        else: return None
    
    def print_deck(self): 
        if self._visibility == 1: 
            return self.__card_list
        else: return None

