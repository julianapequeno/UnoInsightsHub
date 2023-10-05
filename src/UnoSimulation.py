from dataclasses import dataclass
from CircularVector import CircularVector
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
            self.CURRENTLY_PLAYER = []
            self.initialize_players()
        else:
            self.STATUS_CAN_PLAY = False
        
    def initialize_players(self): 
        
        self.IA_PLAYERS_CIRCULAR_VECTOR = CircularVector(self.number_of_players)
        
        for i in range(0,self.number_of_players):
            ia_player = PlayerStrategy1("Player "+str(i),self.bot)
            cards = self.bot.return_player_first_hand()
            ia_player.receive_first_hand(cards)

            initial_cards_of_player = [str(n) for n in cards]
            #storing initial cards
            self.initial_cards.insert(i,initial_cards_of_player)
            
            #adding player to the game
            self.IA_PLAYERS_CIRCULAR_VECTOR.add(ia_player)
      
    def print_cant_run_UNO_error_message(self):
        print("Sorry. The number of players is either exceding the limit or under the minimum number")
    
    def reset_simulation(self):
        self.bot.reset_uno_machine()
        self.CARD_ON_THE_TABLE = None
        self.CURRENTLY_PLAYER = []
        self.initial_cards = []
        self.initialize_players()
        
    def initialize_game_first_card(self):
        #draw a brand new card from deck
        self.CARD_ON_THE_TABLE =  self.bot.take_new_card_from_deck()
        
        #discart card from avaiable cards
        self.bot.discart_a_card(self.CARD_ON_THE_TABLE)
        
        #change currently card to CARD_ON_THE_TABLE
        self.bot.change_currently_card(self.CARD_ON_THE_TABLE) 
     
    def shuffle_cards(self):
        self.bot.shuffle_cards()
        
    def update_currently_player(self):
        self.CURRENTLY_PLAYER = self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(self.bot.INDEX_WHO_IS_PLAYING)
        
    def round(self) -> Output:
        if self.STATUS_CAN_PLAY:
            self.print_simulation_scrip()
            
            self.shuffle_cards()
            self.initialize_game_first_card()
            
            self.print_game_beggining(self.CARD_ON_THE_TABLE)
            
            while(True):
                self.update_currently_player()
                
                self.bot.check_if_deck_is_empty_and_refuel_deck()
                    
                card_thrown = self.CURRENTLY_PLAYER.move()
                
                if card_thrown != None: #player's not passed his turn 
                    self.CARD_ON_THE_TABLE = card_thrown
                    print(self.CURRENTLY_PLAYER.get_player_name()," >>>>> ",self.CARD_ON_THE_TABLE," <<<<<<")
                    
                    self.check_if_is_uno()
                    
                    if(self.player_has_won()): #simulation 
                        name = self.CURRENTLY_PLAYER.get_player_name()
                        return self.simulation_data(name)
                
                    #execute card action
                    card_thrown.execute_move(self.bot,self.IA_PLAYERS_CIRCULAR_VECTOR)
                        
                else:
                    print(self.CURRENTLY_PLAYER.get_player_name()," has passed their turn")
                
                self.bot.INDEX_WHO_IS_PLAYING += 1
        else:
            self.print_cant_run_UNO_error_message()
            return None
    
    def check_if_is_uno(self):
        if(self.bot.is_UNO(self.bot.uno_deck.get_cards_length())): 
            print("UNO!! - ",self.CURRENTLY_PLAYER.get_player_name())
                
    def player_has_won(self):
        if(self.bot.winner(self.bot.uno_deck.get_cards_length())):
            print(self.CURRENTLY_PLAYER.get_player_name(), ' won the game')
            return True
        else:
            return False
                            
    def simulation_data(self,name):
        initial_hands = self.initial_cards
        out = Output(name,initial_hands)
        self.reset_simulation() #reset the simulation
        return out
           
    def print_simulation_scrip(self):
        print(">>>>>>>>> Launching UNO")
        print("Simulating with ",self.number_of_players," players")
        print("* PLAYERS INITIAL CARDS: ")
        
        print(self.IA_PLAYERS_CIRCULAR_VECTOR)
        for i in range(0, self.number_of_players):
            print(">>>> Player ",i)
            lista_add = []
            for card in self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(i).get_player_cards():
                print("Card [",card.rank,",",card.color,"]")

    def print_game_beggining(self,card):
        print(">> INITIAL CARD: ",card)
        print(">>>>>>>> GAME BEGINS >>>>>>>>>")

if __name__=='__main__':
    uno = UnoSimulation(4)
    uno.round()