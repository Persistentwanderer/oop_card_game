class Strategy(): 
    def __init__(self): 
        self.strategies = []
    
    def chose_card(self, source, destination): 
        for card in source: 
            print(card)


class Greedy(Strategy): 
    def __init__(self, motivation): 
        super().__init__(self)

class Random(Strategy): 
    def __init__(self): 
        super().__init__(self)





