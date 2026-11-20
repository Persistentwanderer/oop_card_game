
class Card(): 
    def __init__(self, value = None, suit = None, **kwargs): 
        self.value = value 
        self.suit = suit
        # for arg in kwargs:
        #     self.(str(arg)) = arg
        if enhancement: self.enhancement = enhancement
        if series: self.series = series

    @property
    def value(self): 
        return self.__value

    @setter
    def value(self, value):
        self.__value = value
    
    @property
    def suit(self): 
        return self.__suit

    @setter
    def value(self, suit):
        self.__suit = suit 


class Attribute(Card):
    def __init__(self, value, suit, *args): 
        super().__init__(value, suit)
