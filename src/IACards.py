from UnoDeck import UnoDeck
import random

class IACards:
    def __init__(self):
        self.uno = UnoDeck()
        self.currently_card = []
        
    def get_uno(self):
        return self.uno
    
    uno = property(get_uno)
        
    def entrega_mao_do_jogador(self):
        nova_mao = random.sample(self.uno.cards,7) 
        self.delete_cards_from_deck(nova_mao)
        return nova_mao
        
    def delete_cards_from_deck(self,cards):
        for card in cards:
            self.uno.cards.remove(card)
        
    def take_new_card_from_deck(self): 
        new_card = random.sample(self.uno.cards,1)
        self.delete_cards_from_deck(new_card)
        return new_card[0]
    
    def discart_a_card(self,card):
        #adiciona a nova carta à pilha de descarte
        self.uno.discart_pile.append(card)
        self.currently_card = card
        
    def refuel_deck(self): #reabastecer com a pilha morta
        self.uno.cards = self.uno.discart_pile
        first_element_of_new_pile = self.uno.cards.pop() 
        
        self.uno.discart_pile.clear()
        self.uno.discart_pile.append(first_element_of_new_pile) 
        
        
    def shuffle_cards(self):
        random.shuffle(self.uno.cards)
        
    def deck_is_null(self):
        if len(self.uno.cards) == 0:
            return True
        else:
            return False    
