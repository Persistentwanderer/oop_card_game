import Strategy

class Player(): 
    def __init__(self, name):
        self.name = name 

    def play(self, source, destination): 
        for card in 