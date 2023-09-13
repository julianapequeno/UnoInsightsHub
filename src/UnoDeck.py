import random 
import collections

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
  
  def draw_new_hand(self):
    return random.sample(self.cards,7)
  
  def discart_a_card(self,card):
    #adiciona a nova carta à pilha de descarte
    self.discart_pile.append(card)
  
  def take_new_card_from_deck(self): #to draw a card #puxar da pilha
    new_card = random.sample(self.cards,1)
    self.cards.remove(new_card[0])
    return new_card[0]

  def delete_card_from_deck(self,card):
    self.cards.remove(card)

  def block_action_card(self):
    pass

  def refuel_deck(self): #reabastecer com a pilha morta
    self.cards = self.discart_pile
    first_element_of_new_pile = self.cards.pop() # apaga o último, que ficará na pilha morta
    self.dicart_pile.clear()
    self.discart_pile.append(first_element_of_new_pile) #inicia com a última carta


  def block_card(self,index):
    return index+1 #pula um player
  
  def reverse_card(self,lista):
    return lista.inverter()

  def add_two_cards(self):
    if len(self.cards) < 2:
      self.refuel_deck()
    
    new_two_cards = [self.take_new_card_from_deck() for i in range(0,2)]
    return new_two_cards
  
  def add_four_cards(self):
    if len(self.cards) < 4:
      self.refuel_deck()

    new_four_cards = [self.take_new_card_from_deck() for i in range(0,2)]
    return new_four_cards
  
  def choose_a_new_color_card(self):
    return random.sample(self.colors,1)

  def action_cards(self,card):
    if(card[0] == 'X'): # BLOQUEIO
      return self.block_card
    elif(card[0] == 'R'): # REVERSO
      return self.reverse_card
    elif(card[0] == '+'): #SOMA DOIS
      return self.add_two_cards
    elif(card[0] == 'W'): # SOMA QUATRO
      return self.add_four_cards
    elif(card[0] == 'C'): # ESCOLHA A COR
      return self.choose_a_new_color_card
