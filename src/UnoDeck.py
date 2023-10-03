from Card import Card
from ActionCards import ActionCard
from CardsBehaviors import *

class UnoDeck:

  colors = 'blue yellow red green'.split()
  
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