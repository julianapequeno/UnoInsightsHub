class Player:
  def __init__(self,name,cards):
    self._name = name
    self._player_cards = cards

  def get_name(self):
    return self._name

  def get_cards(self):
    return self._player_cards
  
  def throw_card(self,throw_this_card):
    self._player_cards.remove(throw_this_card)
  
  def get_new_card(self,new_card):
    self._player_cards.append(new_card)

  def get_quantity_cards(self):
    return len(self._player_cards)