from UnoDeck import UnoDeck
import random

class IA_UNO:
    def __init__(self):
        self.uno_deck = UnoDeck()
        
    def block_card_action(self):
        return ['X',1]
    
    def reverse_card_action(self):
        return ['R',0]

    def take_two_cards_action(self):
        if len(self.uno_deck.cards) < 2:
            self.refuel_deck()
        
        #new_two_cards = [self.take_new_card_from_deck() for i in range(0,2)]
        return ['+']
    
    def take_four_cards_action(self):
        if len(self.uno_deck.cards) < 4:
            self.refuel_deck()

        #new_four_cards = [self.take_new_card_from_deck() for i in range(0,4)]
        return ['W']
    
    def choose_a_new_color_card_action(self):
        return ['C',random.sample(self.uno_deck.colors,1)]
  
    def refuel_deck(self): 
        self.uno_deck.cards = self.uno_deck.discart_pile
        first_element_of_new_pile = self.uno_deck.cards.pop() 
        
        self.uno_deck.discart_pile.clear()
        self.uno_deck.discart_pile.append(first_element_of_new_pile) 

    def default(self):
        return ["D","default"]
