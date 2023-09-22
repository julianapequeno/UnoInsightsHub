import random
from Player import Player

class IA_PLAYER:
    ESTRATEGY = {'':1} #list of possible estrategies

    def __init__(self, name, ia_uno):
        self.me_player = Player(name)
        self.IA_UNO = ia_uno

    def receive_first_hand(self,cards):
        self.me_player.my_cards = cards
        
    def throw_card_away(self,card):
        self.me_player.throw_a_card(card) #deleting in player's hand
        self.IA_UNO.discart_a_card(card) #adding to the discart pile

    def draw_from_deck(self,card):
       self.me_player.take_a_new_card(card)
    
    def move(self) : # the player's move
        list_of_possible_throws = self.possible_throws()
        return_card = ['D']
        if(len(list_of_possible_throws) == 0): #user takes another card
            new_card = self.IA_UNO.take_new_card_from_deck()
            self.draw_from_deck(new_card)
            
            if(self.IA_UNO.card_can_be_throw(new_card)):
                return_card = new_card
                self.throw_card_away(new_card)
        else:  
            aleatory_card = random.sample(list_of_possible_throws,1) #pega uma aleatória entre as possíveis
            return_card =  aleatory_card
            self.throw_card_away(aleatory_card[0])

        if self.is_UNO():
            print("UNO")
            return list("U")
        elif self.winner():
            return list("G")
        return return_card
    
    def possible_throws(self): #retorna a lista de possíveis jogadas
        list_of_possible_throws = []
        for play_card in self.me_player.my_cards:
            if(self.IA_UNO.card_can_be_throw(play_card)):
                list_of_possible_throws.append(play_card)
        return list_of_possible_throws
    
    def is_UNO(self):
        if(len(self.me_player.get_player_cards()) == 1):
            return True
        else:
            return False     
    def winner(self):
        if(len(self.me_player.get_player_cards()) == 0):
            return True
        else:
            return False
    

        
        
    
    