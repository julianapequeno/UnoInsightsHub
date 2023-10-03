from Card import Card
from CardsBehaviors import Behavior

#class of ActionCard extends from Card
class ActionCard(Card):
    def __init__(self, rank, color, behavior:Behavior)->None:
        super().__init__(rank,color)
        self.behavior = behavior
    
    def execute_move(self,machine):
        self.behavior.execute(machine)