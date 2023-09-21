import random 
import collections

from VetorCircular import VetorCircular

class UnoDeck:

  uno = collections.namedtuple('Card',['rank','color'])

  ranks = [str(n) for n in range(0,11)] + list('XXRR++WC') #X -> BLOQUEIO ; R -> REVERSE ; + -> SOMA DOIS ; W -> SOMA QUATRO ; C -> ESCOLHA A COR (CHOICE)
  colors = 'blue yellow red green'.split()

  def __init__(self):
    self.cards = [self.uno(rank,color) for color in self.colors for rank in self.ranks]
    self.discart_pile = []

  def __len__(self):
    return len(self._cards)

  def __getitem__(self,position):
    return self._cards[position]
  
  def get_cards(self):
    return self.cards
  
  def get_discart_pile(self):
    return self.discart_pile
  
  def set_cards(self,cards):
    self.cards = cards
  
  #cards = property(get_cards,set_cards)
  #discart_pile = property(get_discart_pile)

  def block_card(self):
    return ['X',1] #pula um player
  
  def reverse_card(self):
    return ['R',0]

  def add_two_cards(self):
    if len(self.cards) < 2:
      self.refuel_deck()
    
    #new_two_cards = [self.take_new_card_from_deck() for i in range(0,2)]
    return ['+']
  
  def add_four_cards(self):
    if len(self.cards) < 4:
      self.refuel_deck()

    #new_four_cards = [self.take_new_card_from_deck() for i in range(0,4)]
    return ['W']
  
  def choose_a_new_color_card(self):
    return ['C',random.sample(self.colors,1)]
  
  def default(self):
    return ["D","default"]

  def action_cards(self,card):
    if(card[0] == 'X'): # BLOQUEIO
      return self.block_card()
    elif(card[0] == 'R'): # REVERSO
      return self.reverse_card()
    elif(card[0] == '+'): #SOMA DOIS
      return self.add_two_cards()
    elif(card[0] == 'W'): # SOMA QUATRO
      return self.add_four_cards()
    elif(card[0] == 'C'): # ESCOLHA A COR
      return self.choose_a_new_color_card()
    else:
      return self.default()
    
    
  def refuel_deck(self): #reabastecer com a pilha morta
        self.cards = self.discart_pile
        first_element_of_new_pile = self.cards.pop() 
        
        self.discart_pile.clear()
        self.discart_pile.append(first_element_of_new_pile) 
