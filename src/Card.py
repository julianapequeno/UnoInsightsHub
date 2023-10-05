#class of Card
class Card:
    def __init__(self, rank, color)->None:
        self.rank = rank
        self.color = color
    
    def __str__(self) -> str:
        return str("Card ("+str(self.rank)+" ,"+self.color+")")
        
    def execute_move(self,machine,players): 
        pass