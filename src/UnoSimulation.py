from VetorCircular import VetorCircular
from IA_UNO import IA_UNO
from IA_Player import IA_PLAYER

class UnoSimulation:
    
    def __init__(self, number_of_players=4):
        self.IA_UNO = IA_UNO()
        
        self.number_of_players = number_of_players    
        self.initialize_players()
    
        self.index_who_is_playing = 0 
        
    def initialize_players(self): 
        self.players = VetorCircular(self.number_of_players)
        for i in range(0,self.number_of_players):
            player = IA_PLAYER("Player "+str(i+1))
            player.receive_first_hand(self.IA_UNO.return_player_first_hand())
            self.players.adicionar(player)
    
    def round(self):
        self.IA_UNO.shuffle_cards() 
        self.IA_UNO.card_on_the_table =  self.IA_UNO.take_new_card_from_deck()#initial card


if __name__=='__main__':
    uno = UnoSimulation()
    uno.round()