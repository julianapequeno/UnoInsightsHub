from src.entity.Card import Card
from src.entity.CardsBehaviors import Behavior

#class of ActionCard extends from Card
class ActionCard(Card):
    def __init__(self, rank, color, behavior:Behavior)->None:
        super().__init__(rank,color)
        self.behavior = behavior
    
    def execute_move(self,machine,players):
        self.behavior.execute(machine,players)