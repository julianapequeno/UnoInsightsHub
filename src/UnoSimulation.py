from dataclasses import dataclass
from CircularVector import CircularVector
from Machine import Machine
from PlayerStrategy1 import PlayerStrategy1

@dataclass
class SimulationOutputData:
    winner: str
    first_players_hands: list[list[str]]
    
@dataclass
class SimulationInputData:
    bot: Machine
    round_players: CircularVector
    number_of_players: int

class UnoSimulation:
    
    STATUS_CAN_PLAY = False
    
    def __init__(self,input:SimulationInputData):
        self.bot = input.bot
        self.number_of_players = input.number_of_players
        self.verify_initial_parameters()
        
        if(self.STATUS_CAN_PLAY):
            self.IA_PLAYERS_CIRCULAR_VECTOR = input.round_players
            self.initialize_players()
    
    def verify_initial_parameters(self):
        self.STATUS_CAN_PLAY = self.bot.can_this_number_of_players_play_uno(self.number_of_players)
    
    def initialize_players(self): 
        self.INITIAL_PLAYERS_CARDS = []
        
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            #insert bot into ia_player
            ia_player.insert_uno_machine(self.bot)
            
            #insert cards into players
            cards = self.bot.get_player_first_hand()
            ia_player.player.setcards(cards)
            
            #storing initial cards
            initial_cards_of_player = [str(n) for n in cards]
            self.INITIAL_PLAYERS_CARDS.insert(i,initial_cards_of_player)
    
    def reset_simulation(self):
        #reset machine
        self.bot.reset_machine()
        
        #reset mainly variables
        self.CARD_ON_THE_TABLE = None
        self.CURRENTLY_PLAYER = []
        self.INITIAL_PLAYERS_CARDS = []
        
    def initialize_game_with_first_card(self):
        self.CARD_ON_THE_TABLE =  self.bot.get_game_first_card()
        
    def update_currently_player(self):
        self.CURRENTLY_PLAYER = self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(self.bot.INDEX_WHO_IS_PLAYING)
        
    def round(self) -> SimulationOutputData:
        if self.STATUS_CAN_PLAY:
            self.print_simulation_scrip()
            
            self.bot.shuffle_cards()
            self.initialize_game_with_first_card()
            
            self.print_game_beggining(self.CARD_ON_THE_TABLE)
            
            while(True):
                self.update_currently_player()
                self.bot.check_if_deck_is_empty_and_refuel_deck()
                
                ##
                next_player_number_of_cards = len(self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(self.bot.INDEX_WHO_IS_PLAYING+1).get_player().cards)
                self.CURRENTLY_PLAYER.get_other_players_number_of_cards(next_player_number_of_cards)
                ##
                
                card_thrown = self.CURRENTLY_PLAYER.move()
                
                if card_thrown != None: #player's not passed his turn 
                    self.CARD_ON_THE_TABLE = card_thrown
                    print(self.CURRENTLY_PLAYER.get_player_name()," > ",self.CARD_ON_THE_TABLE," e agora tem ",len(self.CURRENTLY_PLAYER.get_player().cards))
                    
                    self.check_if_is_uno()
                    
                    if(self.player_has_won()): #simulation 
                        print(self.CURRENTLY_PLAYER.get_player_name()+' won the game')
                        
                        name = self.CURRENTLY_PLAYER.get_player_name()
                        return self.simulation_data(name)
                
                    card_thrown.execute_move(self.bot,self.IA_PLAYERS_CIRCULAR_VECTOR)
                
                else:
                    print(self.CURRENTLY_PLAYER.get_player_name()+" has passed their turn")
                
                self.bot.INDEX_WHO_IS_PLAYING += 1
        else:
            self.print_cant_run_UNO_error_message()
            return None
    
    def check_if_is_uno(self):
        if(self.bot.is_UNO(self.CURRENTLY_PLAYER.get_player_cards())): 
            print("UNO!! - "+self.CURRENTLY_PLAYER.get_player_name())
                
    def player_has_won(self):
        return self.bot.winner(self.CURRENTLY_PLAYER.get_player_cards())
                            
    def simulation_data(self,name):
        initial_hands = self.INITIAL_PLAYERS_CARDS
        out = SimulationOutputData(name,initial_hands)
        self.reset_simulation() #reset the simulation
        return out
    
    def print_simulation_scrip(self):
        print(">>>>>>>>> Launching UNO")
        print(f"Simulating with {self.number_of_players} players")
        print("* PLAYERS INITIAL CARDS: ")
        
        print(self.IA_PLAYERS_CIRCULAR_VECTOR)
        for i in range(0, self.number_of_players):
            print(">>>> Player ",i)
            for card in self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(i).get_player_cards():
                print(f"Card [{card.rank},{card.color}]")

    def print_game_beggining(self,card):
        print(">> INITIAL CARD: ",str(card))
        print(">>>>>>>>>>>>>>>>> GAME BEGINS")

    def print_cant_run_UNO_error_message(self):
        print("Sorry. The number of players is either exceding the limit or under the minimum number")
    
if __name__=='__main__':
    UNO_MACHINE = Machine()
    PLAYERS = CircularVector(4)
    
    for i in range(0,4):
        player_name = "Player "+str(i)
        ia_player = PlayerStrategy1(player_name)
        PLAYERS.add(ia_player)
            
    simulation_data = SimulationInputData(UNO_MACHINE,PLAYERS,4)
    
    uno = UnoSimulation(simulation_data)
    uno.round()