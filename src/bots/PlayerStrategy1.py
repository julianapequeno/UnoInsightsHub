import random
from entity.ActionCards import ActionCard
from entity.Card import Card
from bots.IA_Player import IA_Player


class PlayerStrategy1(IA_Player):
    ACTION_CARDS: list[ActionCard]
    NORMAL_CARDS: list[Card]
    PRIORITY_TO_THROW_ACTION_CARD = False

    def player_strategy_which_card_throw(self, list_of_possible_throws):
        self.split_action_and_normal_cards(list_of_possible_throws)
        self.identify_if_should_throw_an_action_card()

        if self.PRIORITY_TO_THROW_ACTION_CARD and self.ACTION_CARDS:
            card = random.sample(self.ACTION_CARDS, 1)
            return card[0]
        else:
            card = random.sample(list_of_possible_throws, 1)
            return card[0]

    def split_action_and_normal_cards(self, list_of_possible_throws):
        self.ACTION_CARDS = []
        self.NORMAL_CARDS = []

        for card in list_of_possible_throws:
            if isinstance(card, ActionCard):
                self.ACTION_CARDS.append(card)
            else:
                self.NORMAL_CARDS.append(card)

    def identify_if_should_throw_an_action_card(self):
        if self.NEXT_PLAYER_NUMBER_OF_CARDS <= 4:
            self.PRIORITY_TO_THROW_ACTION_CARD = True
