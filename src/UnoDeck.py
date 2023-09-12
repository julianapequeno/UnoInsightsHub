import random 
import collections

uno = collections.namedtuple('Card',['rank','color'])

class UnoDeck:

  ranks = [str(n) for n in range(0,11)] + list('XXRR++WC') #X -> BLOQUEIO ; R -> REVERSE ; + -> SOMA DOIS ; W -> SOMA QUATRO ; C -> ESCOLHA A COR (CHOICE)
  colors = 'blue yellow red green'.split()

  def __init__(self):
    self.cards = [uno(rank,color) for color in self.colors for rank in self.ranks]
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
    #print(new_card)
    self.cards.remove(new_card[0])
    return new_card

  def delete_card_from_deck(self,card):
    self.cards.remove(card)

  def block_action_card(self):
    pass

  
  
  # def action_cards(self,card):
    # if(card[0] == 'X'): # BLOQUEIO

    # elif(card[0] == 'R'): # REVERSO

    # elif(card[0] == '+'): #SOMA DOIS

    # elif(card[0] == 'W'): # SOMA QUATRO

    # elif(card[0] == 'C'): # ESCOLHA A COR

