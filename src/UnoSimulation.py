from VetorCircular import VetorCircular
from IA_UNO import IA_UNO
from IA_Player import IA_PLAYER

class UnoSimulation:
    
    def __init__(self, number_of_players=4):
        self.IA_UNO = IA_UNO()

        self.number_of_players = number_of_players    
        self.initialize_players()
        
    def initialize_players(self): 
        self.IA_UNO.my_players = VetorCircular(self.number_of_players)
        for i in range(0,self.number_of_players):
            player = IA_PLAYER("Player "+str(i),self.IA_UNO)
            player.receive_first_hand(self.IA_UNO.return_player_first_hand())
            self.IA_UNO.my_players.adicionar(player)
    
    def round(self):
        self.print_simulate_scrip()
        
        self.IA_UNO.shuffle_cards() 
        
        self.card_on_the_table =  self.IA_UNO.take_new_card_from_deck()
        self.IA_UNO.discart_a_card(self.card_on_the_table)
        
        self.IA_UNO.change_currently_card(self.card_on_the_table)
        
        
        self.print_game_beggining(self.card_on_the_table)
        
        while(True):
            self.who_is_currently_playing = self.IA_UNO.my_players.get_player_by_index(self.IA_UNO.INDEX_WHO_IS_PLAYING)
        
            if len(self.IA_UNO.uno_deck.cards) == 0:
                self.IA_UNO.refuel_deck()
                
            card_thrown = self.IA_UNO.my_players.get_player_by_index(self.IA_UNO.INDEX_WHO_IS_PLAYING).move()    
            
            if not 'P' in card_thrown: #player's not passed his turn 
                self.card_on_the_table = card_thrown
                print(self.who_is_currently_playing.me_player.name," - ",card_thrown[0])
                
                if(self.IA_UNO.is_UNO(len(self.who_is_currently_playing.me_player.get_player_cards()))):
                    print("UNO!! - ",self.who_is_currently_playing.me_player.name)

                if(self.IA_UNO.winner(len(self.who_is_currently_playing.me_player.get_player_cards()))):
                    print(self.IA_UNO.my_players.get_player_by_index(self.IA_UNO.INDEX_WHO_IS_PLAYING).me_player.name, ' won the game')
                    break
               
                if(len(card_thrown) == 2): #has an action card
                    self.IA_UNO.applying_action_card(card_thrown)
            else:
                print(self.who_is_currently_playing.me_player.name," has passed his turn")
            
            self.IA_UNO.INDEX_WHO_IS_PLAYING += 1
            
    def print_simulate_scrip(self):
        print(">>>>>>>>> Launching UNO")
        print("Simulating with ",self.number_of_players," players")
        print("* PLAYERS INITIAL CARDS: ")
        
        for i in range(0, self.number_of_players):
            print(">>>> Player ",i)
            for card in self.IA_UNO.my_players.get_player_by_index(i).me_player.my_cards:
                print(card[0],' - ',card[1])
        print(">> shuffling cards...")

    def print_game_beggining(self,card):
        print(">> INITIAL CARD: ",card)
        print(">>>>>>>> GAME BEGINS >>>>>>>>>")

if __name__=='__main__':
    uno = UnoSimulation()
    uno.round()
    print(">>>> Simulation finalized with sucess")