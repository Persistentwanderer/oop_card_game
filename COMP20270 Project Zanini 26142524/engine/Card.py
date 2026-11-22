
class Card(): 
    def __init__(self, value, suit, **kwargs): 
        self.value = value
        self.suit= suit

    @property
    def value(self, value): 
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
    @property
    def suit(self,suit): 
        return self.__suit

    @suit.setter
    def suit(self, suit):
        self.__suit = suit 

    def __str__(self): 
        return f"Value: {self.__value}\tSuit: {self.__suit}"


class Attribute(Card):
    def __init__(self, value, suit, **kwargs): 
        super().__init__(value, suit)
        # for attribute in 
        self.attribute = "attribute"