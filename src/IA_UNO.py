from UnoDeck import UnoDeck
import random

class IA_UNO:
    
    def __init__(self):
        self.uno_deck = UnoDeck()
        self.CURRENTLY_CARD = []
        self.INDEX_WHO_IS_PLAYING = 0 
        self.players = []
    
    def shuffle_cards(self):
        random.shuffle(self.uno_deck.cards)
        
    def change_currently_card(self,card):
        self.CURRENTLY_CARD = card
    
    def discart_a_card(self,card):
        #adiciona a nova carta à pilha de descarte
        self.uno_deck.discart_pile.append(card)
        self.CURRENTLY_CARD = card
        
    def take_new_card_from_deck(self): 
        new_card = random.sample(self.uno_deck.cards,1)
        self.delete_cards_from_deck(new_card)
        return new_card[0]
           
    def block_card_action(self):
        self.INDEX_WHO_IS_PLAYING += 1
    
    def reverse_card_action(self):
        self.players.vetor.reverse()


    def take_two_cards_action(self):
        if len(self.uno_deck.cards) < 2:
            self.refuel_deck()
        
        new_two_cards = [self.take_new_card_from_deck() for i in range(0,2)]
        return new_two_cards
    
    def take_four_cards_action(self):
        if len(self.uno_deck.cards) < 4:
            self.refuel_deck()

        new_four_cards = [self.take_new_card_from_deck() for i in range(0,4)]
        return new_four_cards
    
    def choose_a_new_color_card_action(self):
        return random.sample(self.uno_deck.colors,1)
  
    def refuel_deck(self): 
        self.uno_deck.cards = self.uno_deck.discart_pile
        first_element_of_new_pile = self.uno_deck.cards.pop() 
        
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
        if(card[0] == 'X'): # BLOQUEIO
            self.block_card_action()
        elif(card[0] == 'R'): # REVERSO
            self.reverse_card_action()
        elif(card[0] == '+'): #SOMA DOIS 
            for card in self.take_two_cards_action():
                self.players.get_player_by_index(self.INDEX_WHO_IS_PLAYING+1).player.get_new_card(card)
        elif(card[0] == 'W'): #SOMA QUATRO
            for card in self.take_four_cards_action():
                self.players.get_player_by_index(self.INDEX_WHO_IS_PLAYING+1).player.get_new_card(card)
        elif(card[0] == 'C'): # ESCOLHA A COR
            self.CURRENTLY_CARD[1] = self.choose_a_new_color_card_action()