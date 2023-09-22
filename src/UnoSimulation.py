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
            player = IA_PLAYER("Player "+str(i+1),self.IA_UNO)
            player.receive_first_hand(self.IA_UNO.return_player_first_hand())
            self.players.adicionar(player)
        print(self.players.get_player_by_index(0).me_player.my_cards)
    
    def round(self):
        self.IA_UNO.shuffle_cards() 
        self.card_on_the_table =  self.IA_UNO.take_new_card_from_deck()
        self.IA_UNO.change_currently_card(self.card_on_the_table)
        
        while(True):
            if len(self.IA_UNO.uno_deck.cards) == 0:
                self.IA_UNO.refuel_deck()
            card_thrown = self.players.get_player_by_index(self.index_who_is_playing).move()    

            if(card_thrown[0] == 'G'):
                print(self.players.get_player_by_index(0).me_player.name)
                break
            self.index_who_is_playing += 1

if __name__=='__main__':
    uno = UnoSimulation()
    uno.round()