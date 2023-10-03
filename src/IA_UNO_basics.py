from src.UnoDeck import UnoDeck
import random

class IA_UNO_basics:
    
    def __init__(self):
        self.uno_deck = UnoDeck()
        self.CURRENTLY_CARD = []
        self.INDEX_WHO_IS_PLAYING = 0 
        self.players = []
        self.STILL_A_ROUND_OF_7 = False
        
    def get_players(self):
        return self.players
    
    def set_players(self,players):
        self.players = players
        
    my_players = property(get_players,set_players)
        
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
        
    def shuffle_cards(self):
        random.shuffle(self.uno_deck.cards)
        
    def change_currently_card(self,card):
        self.CURRENTLY_CARD = card
    
    def discart_a_card(self,card):
        #adiciona a nova carta à pilha de descarte
        self.uno_deck.discart_pile.append(card)
        self.CURRENTLY_CARD = card

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
