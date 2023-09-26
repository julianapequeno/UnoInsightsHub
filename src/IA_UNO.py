from UnoDeck import UnoDeck
from ActionCards import ActionCards

import random

class IA_UNO:
    
    def __init__(self):
        self.uno_deck = UnoDeck()
        self.CURRENTLY_CARD = []
        self.INDEX_WHO_IS_PLAYING = 0 
        self.players = []
        self.STILL_A_ROUND_OF_7 = False
        self.ACTION_CARD = ActionCards()
        
    def get_players(self):
        return self.players
    
    def set_players(self,players):
        self.players = players
        
    my_players = property(get_players,set_players)
    
    def shuffle_cards(self):
        random.shuffle(self.uno_deck.cards)
        
    def change_currently_card(self,card):
        self.CURRENTLY_CARD = card
    
    def discart_a_card(self,card):
        #adiciona a nova carta à pilha de descarte
        self.uno_deck.discart_pile.append(card)
        self.CURRENTLY_CARD = card
        
    def take_new_card_from_deck(self): 
        if len(self.uno_deck.cards) == 0:
            self.refuel_deck()
            
        new_card = random.sample(self.uno_deck.cards,1)
        self.delete_cards_from_deck(new_card)
        return new_card[0]
           
    def refuel_deck(self): 
        self.uno_deck.cards = self.uno_deck.cards+self.uno_deck.discart_pile
        first_element_of_new_pile = self.uno_deck.cards.pop(0) 
        
        self.uno_deck.discart_pile.clear()
        self.uno_deck.discart_pile.append(first_element_of_new_pile) 

    def return_player_first_hand(self):
        hand = random.sample(self.uno_deck.cards,7) 
        self.delete_cards_from_deck(hand)
        return hand
    
    def delete_cards_from_deck(self,cards):
        for card in cards:
            self.uno_deck.cards.remove(card)

    def card_can_be_throw(self,card): #verifica se a carta pode ser jogada
        if (card[1] == self.CURRENTLY_CARD[1]) or (card[0] == self.CURRENTLY_CARD[0]):
            return True
        return False  
    
    def applying_action_card(self,card):
        if(card[0][0] == 'X'): # BLOQUEIO
           # self.block_card_action()
            self.INDEX_WHO_IS_PLAYING = self.ACTION_CARD.block_card_action(self.INDEX_WHO_IS_PLAYING)
    
        elif(card[0][0] == 'R'): # REVERSO
           # self.reverse_card_action()
            self.INDEX_WHO_IS_PLAYING = self.ACTION_CARD.reverse_card_action(self.players, self.INDEX_WHO_IS_PLAYING)
         
        elif(card[0][0] == '+'): #SOMA DOIS 
            if self.should_refuel_deck():
                self.refuel_deck()
                
            new_two_cards = [self.take_new_card_from_deck() for i in range(0,2)]
             
            for card in new_two_cards:
                self.players.get_player_by_index(self.INDEX_WHO_IS_PLAYING+1).me_player.take_a_new_card(card)

        elif(card[0][0] == 'W'): #SOMA QUATRO
            if self.should_refuel_deck():
                self.refuel_deck()
                
            new_four_cards = [self.take_new_card_from_deck() for i in range(0,4)]
             
            for card in new_four_cards:
                self.players.get_player_by_index(self.INDEX_WHO_IS_PLAYING+1).me_player.take_a_new_card(card)
       
        elif(card[0][0] == 'C'): # ESCOLHA A COR
            self.CURRENTLY_CARD = self.uno_deck.uno(card[0],self.ACTION_CARD.choose_a_new_color_card_action(self.uno_deck))
        
        #numbers cards action
        elif(card[0][0] == '0'): #can change hands with other person
            self.ACTION_CARD.zero_action_card(self.players,self.INDEX_WHO_IS_PLAYING)
        elif(card[0][0] == '9'): #bater na mesa
            pass
            
      #  if(card[0][0] == '7' or self.STILL_A_ROUND_OF_7): #silence
        #    if(card[0][0] == '7'):
         #       self.STILL_A_ROUND_OF_7 = True
          #      self.seven_count = 1
           # self.ACTION_CARD.seven_action_card(self.players)
            #self.seven_count +=1
            
            #if(self.seven_count == len(self.players)):
             #   self.STILL_A_ROUND_OF_7 = False
                 
    
    def should_refuel_deck(self):
        if len(self.uno_deck.cards) < 2:
            return True   
        
        if len(self.uno_deck.cards) < 4:
            return True   
    
    def is_UNO(self,cards):
        if(cards == 1):
            return True
        else:
            return False     

    def winner(self, cards):
        if(cards == 0):
            return True
        else:
            return False 