from Card import Card
from ActionCards import ActionCard
from CardsBehaviors import *

class UnoDeck:

  colors = 'blue yellow red green'.split()
  min_cards_on_deck = 4
  number_of_cards_for_each_player = 7
  
  def __init__(self):
    self.cards = []
    self.discart_pile = []
    
    #adding common cards to deck
    for color in self.colors:
      self.cards.append(Card(0,color))
      for i in range(1,10):
        self.cards.append(Card(i,color))
        self.cards.append(Card(i,color))
        
    #adding action and wild cards to deck
    for color in self.colors:
        self.cards.append(ActionCard('X',color,BlockNextPlayer))
        self.cards.append(ActionCard('X',color,BlockNextPlayer))
        self.cards.append(ActionCard('R',color,Reverse))
        self.cards.append(ActionCard('R',color,Reverse))
        self.cards.append(ActionCard('+',color,DrawTwoCards))
        self.cards.append(ActionCard('+',color,DrawTwoCards))
        self.cards.append(ActionCard('W',color,DrawFourCards))
        self.cards.append(ActionCard('C',color,ChangeColor))
      
  def get_cards_length(self):
    return len(self.cards)

  def can_this_number_of_players_play_uno(self, number_of_players):
    if ((len(self.cards)-self.min_cards_on_deck)/self.number_of_cards_for_each_player) < number_of_players:
        return False
    elif(number_of_players < 1):
        return False
    else:
        return True

  def need_to_refuel_deck(self):
    return len(self.cards) == 0
  
  def draw_a_card_from_deck(self):
    new_card = random.sample(self.cards,1)
    self.delete_cards_from_deck(new_card)
    return new_card[0]

  def delete_cards_from_deck(self,cards_to_delete):
    for card in cards_to_delete:
        self.cards.remove(card)

  def refuel_deck(self): 
    #getting all remaining cards together 
    self.cards = self.cards+self.discart_pile 
    #get the last one who was thrown 
    first_element_of_new_pile = self.cards.pop(0) 
    #clear discart pile and append the last card thrown
    self.discart_pile.clear()
    self.discart_pile.append(first_element_of_new_pile) 
  
  def shuffle_cards(self):
    random.shuffle(self.cards)
        
  def discart_a_card(self,card):
    self.discart_pile.append(card)
        
  def get_a_uno_hand(self):
    hand = random.sample(self.cards,self.number_of_cards_for_each_player)
    self.delete_cards_from_deck(hand)
    return hand 