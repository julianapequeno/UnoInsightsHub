from dataclasses import dataclass

@dataclass
class Player:
  
  _cards: list
  
  def __init__(self,name):
    self._name = name
    
  @property
  def name(self):
    return self._name
  
  def setcards(self, value): 
    self._cards = value[:]
  
  @property
  def cards(self):
    return self._cards
  
  def delete_card_from_list(self,card):
    self.cards.remove(card)
  
  def add_cart_to_list(self,card):
    self.cards.append(card)
  
  def reset_player(self):
    self.cards.clear()