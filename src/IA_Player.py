
from Player import Player

class IA_PLAYER:
    #ESTRATEGY = enum('Estrategy',['','']) #list of possible estrategies
    ESTRATEGY = {'':1}
    def __init__(self, name):
        self.me_player = Player(name)

    def receive_first_hand(self,cards):
        self.me_player.my_cards = cards
        
        
        
    
    