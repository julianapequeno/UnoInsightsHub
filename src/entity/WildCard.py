from entity.Card import Card
from entity.CardsBehaviors import Behavior


class WildCard(Card):
    def __init__(self, rank, color, behavior: Behavior) -> None:
        super().__init__(rank, color)
        self.behavior = behavior
        self.user_choice = None

    def execute_move(self, machine, players):
        self.behavior.execute(machine, players)
