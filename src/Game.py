from VetorCircular import VetorCircular
from IACards import IACards
from IAPlayer import IAPlayer
from Player import Player

class Game:
    
    def __init__(self, number_of_players=4):
        self.number_of_players = number_of_players
        self.index_who_is_playing = 0 
        self.active_players = VetorCircular(number_of_players)
        self.IA_CARDS = IACards()
        
    def verify_card_action_in_game(self,card_action): # ALGORITMO QUE VERIFICA ON IMPACTO DAS CARTAS JOGADAS NO JOGO
        print(card_action)
        card = card_action[0]
        
        if not card == 'N':
            if(card == 'X'): # BLOQUEIO
                self.index_who_is_playing += int(card_action[1])
                
            elif(card == 'R'): # REVERSO
                self.active_players.vetor.reverse()
                
            elif(card == '+' or card == 'W'): #SOMA DOIS ou QUATRO
                for new_card in card_action:
                    self.active_players.get_player_by_index(self.index_who_is_playing+1).player.get_new_card(new_card)
                
            elif(card == 'C'): # ESCOLHA A COR
                new_color = card_action[1]
                card = self.IA_CARDS.uno.uno(card[0],new_color[0])
            
    def initialize_players(self):
        for i in range(0,self.number_of_players):
            player = IAPlayer(Player("Player "+str(i+1)),self.IA_CARDS)
            self.active_players.adicionar(player)
            
    def rodada(self):
        self.IA_CARDS.shuffle_cards() 
        self.initialize_players() 
        self.IA_CARDS.currently_card =  self.IA_CARDS.take_new_card_from_deck()#initial card
        
        while(True):
           # print("TEMOS ",str(len(self.IA_CARDS.get_uno().cards))," cartas ativas")
            #print("ON THE TABLE: ", self.IA_CARDS.currently_card)
            self.who_is_currently_playing = self.active_players.get_player_by_index(self.index_who_is_playing)
            
            #print(self.who_is_currently_playing.player.get_name()," is playing right now")
            list_card_action = self.who_is_currently_playing.start_player_turn()
            self.verify_card_action_in_game(list_card_action)
            
            if list_card_action[0] == "G":
             #   print(self.who_is_currently_playing.player.get_name()," ganhou!")
                break
            #print("Quantidade de cartas ",len(self.who_is_currently_playing.player.get_player_cards()))
            self.index_who_is_playing += 1

if __name__ == '__main__':
  bot = Game(4)
  bot.rodada()