from UnoDeck import UnoDeck
import random

class Machine:
    
    def __init__(self):
        self.uno_deck = UnoDeck()
        self.CURRENTLY_CARD = []
        self.INDEX_WHO_IS_PLAYING = 0 
    
    def reset_uno_machine(self):
        self.uno_deck = UnoDeck()
        self.CURRENTLY_CARD = []
        self.INDEX_WHO_IS_PLAYING = 0 
    
    def get_uno_deck_cards_length(self):
        return self.uno_deck.get_cards_length()
    
    def can_these_numbers_of_players_play_uno(self, number_of_players):
        min_cards_on_deck = 4
        number_of_cards_for_each_player = 7
        if ((len(self.uno_deck.cards)-min_cards_on_deck)/number_of_cards_for_each_player) < number_of_players:
            return False
        elif(number_of_players < 1):
            return False
        else:
            return True
        
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
        self.uno_deck.discart_pile.append(card)
        self.CURRENTLY_CARD = card

    def return_player_first_hand(self):
        hand = random.sample(self.uno_deck.cards,7) 
        self.delete_cards_from_deck(hand)
        return hand
    
    def delete_cards_from_deck(self,cards):
        for card in cards:
            self.uno_deck.cards.remove(card)

    def card_can_be_throw(self,card): 
        if (card.rank == self.CURRENTLY_CARD.rank) or (card.color == self.CURRENTLY_CARD.color):
            return True
        return False  

    def check_if_deck_is_empty_and_refuel_deck(self):
        if self.get_uno_deck_cards_length() == 0:
            self.refuel_deck()

    def is_UNO(self,cards):
        return cards == 1    

    def winner(self, cards):
        return cards == 0
