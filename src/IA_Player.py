import random
from Card import Card
from Player import Player

class IA_Player():
    
    def __init__(self, name):
        self.player = Player(name)
    
    def insert_uno_machine(self,machine):
        self.UNO_MACHINE = machine
    
    def receive_first_hand(self,cards):
        self.player.my_cards = cards
    
    def get_player(self): 
        return self.player
    
    def get_player_name(self):
        return self.player.name

    def get_player_cards(self):
        return self.player.cards
        
    def throw_card_away(self,card):
        self.player.delete_card_from_list(card) #deleting in player's hand
        self.UNO_MACHINE.discart_a_card(card) #adding to the discart pile

    def draw_from_deck(self,card):
       self.player.add_cart_to_list(card)
       
    def move(self) -> Card : # the player's move
        list_of_possible_throws = self.possible_player_card_throws()
        return_card = None
        
        if(len(list_of_possible_throws) == 0): #user takes another card
            new_card = self.UNO_MACHINE.take_new_card_from_deck()
            self.draw_from_deck(new_card)
            
            if(self.UNO_MACHINE.card_can_be_throw(new_card)):
                return_card = new_card
                self.throw_card_away(new_card)
        else:  
            aleatory_card = self.player_strategy_which_card_throw(list_of_possible_throws)
            
            return_card =  aleatory_card
            self.throw_card_away(aleatory_card)

        return return_card
    
    def possible_player_card_throws(self): 
        list_of_possible_throws = []
        
        for card in self.player.cards:
            if(self.UNO_MACHINE.card_can_be_throw(card)):
                list_of_possible_throws.append(card)
                
        return list_of_possible_throws
    
    def player_strategy_which_card_throw(self,list_of_possible_throws):
        card = random.sample(list_of_possible_throws,1)
        return card[0]

    def get_other_players_number_of_cards(self,players_numbers_of_cards):
        self.NEXT_PLAYER_NUMBER_OF_CARDS = players_numbers_of_cards