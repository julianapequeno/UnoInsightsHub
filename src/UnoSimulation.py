from dataclasses import dataclass
from VetorCircular import VetorCircular
from Machine import Machine
from PlayerStrategy1 import PlayerStrategy1

@dataclass
class Output:
    winner: str
    first_players_hands: list

class UnoSimulation:
    
    STATUS_CAN_PLAY = False
    
    def __init__(self, number_of_players=4):
        self.bot = Machine()
        self.number_of_players = number_of_players
        
        if self.bot.can_these_numbers_of_players_play_uno(number_of_players):
            self.STATUS_CAN_PLAY = True
            self.initial_cards = []
            self.initialize_players()
        else:
            self.STATUS_CAN_PLAY = False

    def print_cant_run_UNO(self):
        print("Sorry. The number of players is either exceding the limit or under the minimum number")
    
    def reset(self):
        self.bot = Machine()
        self.initial_cards = []
        self.initialize_players()
        
    def initialize_players(self): 
        self.bot.my_players = VetorCircular(self.number_of_players)
        
        for i in range(0,self.number_of_players):
            player = PlayerStrategy1("Player "+str(i),self.bot)
            cards = self.bot.return_player_first_hand()
            player.receive_first_hand(cards)

            initial_cards_of_player = [str(n) for n in cards]
            #storing initial cards
            self.initial_cards.insert(i,initial_cards_of_player)
            
            #adding player to the game
            self.bot.my_players.adicionar(player)
     
    def round(self) -> Output:
        if self.STATUS_CAN_PLAY:
            self.print_simulate_scrip()
            self.bot.shuffle_cards() 
            
            self.card_on_the_table =  self.bot.take_new_card_from_deck()
            self.bot.discart_a_card(self.card_on_the_table)
            self.bot.change_currently_card(self.card_on_the_table)
            
            self.print_game_beggining(self.card_on_the_table)
            
            while(True):
                self.who_is_playing = self.bot.my_players.get_ia_player_by_index(self.bot.INDEX_WHO_IS_PLAYING).me_player
                
                if len(self.bot.uno_deck.cards) == 0:
                    self.bot.refuel_deck()
                    
                card_thrown = self.bot.my_players.get_ia_player_by_index(self.bot.INDEX_WHO_IS_PLAYING).move()    
                
                if card_thrown != None: #player's not passed his turn 
                    self.card_on_the_table = card_thrown
                    print(self.who_is_playing.name," >>>>> ",self.card_on_the_table," <<<<<<")
                    
                    if(self.bot.is_UNO(self.who_is_playing.get_cards_len())):
                        print("UNO!! - ",self.who_is_playing.name)
                    
                    if(self.bot.winner(self.who_is_playing.get_cards_len())):
                        print(self.who_is_playing.name, ' won the game')
                        
                        ###############PARA A SIMULAÇÃO
                        name = self.who_is_playing.name
                        return self.simulation_data(name)
                
                    #execute card action
                    card_thrown.execute_move(self.bot)
                        
                else:
                    print(self.who_is_playing.name," has passed their turn")
                
                self.bot.INDEX_WHO_IS_PLAYING += 1
        else:
            self.print_cant_run_UNO()
            return None
    
    def simulation_data(self,name):
        out = Output(name,self.initial_cards)
        self.reset() #reseta a simulação
        return out
           
    def print_simulate_scrip(self):
        print(">>>>>>>>> Launching UNO")
        print("Simulating with ",self.number_of_players," players")
        print("* PLAYERS INITIAL CARDS: ")
        
        for i in range(0, self.number_of_players):
            print(">>>> Player ",i)
            lista_add = []
            for card in self.bot.my_players.get_ia_player_by_index(i).me_player.my_cards:
                print("Card [",card.rank,",",card.color,"]")
        
        print(">> shuffling cards...")

    def print_game_beggining(self,card):
        print(">> INITIAL CARD: ",card)
        print(">>>>>>>> GAME BEGINS >>>>>>>>>")

if __name__=='__main__':
    uno = UnoSimulation(4)
    uno.round()