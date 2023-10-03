class Player:
  def __init__(self,name):
    self._name = name
    self._cards = []

  def get_name(self):
    return self._name

  name = property(get_name)

  def get_player_cards(self):
    return self._cards
  
  def set_player_cards(self,cards):
    self._cards = cards
  
  my_cards = property(get_player_cards,set_player_cards)
  
  def throw_a_card(self,throw_this_card):
    self._cards.remove(throw_this_card)
  
  def take_a_new_card(self,new_card):
    self._cards.append(new_card)

  def get_cards_len(self):
    return len(self._cards)