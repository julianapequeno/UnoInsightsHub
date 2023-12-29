from src.entity.Card import Card
from src.entity.UnoDeck import UnoDeck
from src.entity.WildCard import WildCard
from src.entity.CardsBehaviors import ChangeColor


class Machine:

    def __init__(self):
        self.uno_deck = UnoDeck()
        self.CURRENTLY_CARD: Card
        self.INDEX_WHO_IS_PLAYING = 0
        self.SEVENCARDRUNNING = False
        self.PLAYER_WHO_THROWED_SEVEN_CARD = None

    def reset_machine(self, is_analysis, players_hands_cards):
        self.uno_deck.reset(is_analysis, players_hands_cards)
        self.CURRENTLY_CARD: Card
        self.INDEX_WHO_IS_PLAYING = 0

    def get_uno_deck_cards_length(self):
        return self.uno_deck.get_cards_length()

    def can_this_number_of_players_play_uno(self, number_of_players):
        return self.uno_deck.can_this_number_of_players_play_uno(number_of_players)

    def take_new_card_from_deck(self):
        if self.uno_deck.need_to_refuel_deck():
            self.refuel_deck()

        return self.uno_deck.draw_a_card_from_deck()

    def refuel_deck(self):
        self.uno_deck.refuel_deck()

    def shuffle_cards(self):
        self.uno_deck.shuffle_cards()

    def update_currently_card(self, card):
        self.CURRENTLY_CARD = card

    def discard_a_card(self, card):
        self.uno_deck.discard_a_card(card)
        self.update_currently_card(card)

    def get_player_first_hand(self):
        return self.uno_deck.get_a_uno_hand()

    def delete_cards_from_deck(self, cards):
        self.uno_deck.delete_cards_from_deck(cards)

    def card_can_be_throw(self, card):
        if isinstance(self.CURRENTLY_CARD, WildCard):
            is_change_color_card = (card.rank == self.CURRENTLY_CARD.rank)
            has_same_color = (card.color == self.CURRENTLY_CARD.user_choice)

            if is_change_color_card or has_same_color:
                return True
        else:
            if (card.rank == self.CURRENTLY_CARD.rank) or (
                card.color == self.CURRENTLY_CARD.color
            ):
                return True
        return False

    def check_if_deck_is_empty_and_refuel_deck(self):
        if self.uno_deck.need_to_refuel_deck():
            self.refuel_deck()

    def is_UNO(self, cards):
        return len(cards) == 1

    def winner(self, cards):
        return len(cards) == 0

    def get_game_first_card(self):
        self.CURRENTLY_CARD = self.take_new_card_from_deck()

        # if the game's started with a changecolor card, the next user should verify
        # the compatibility with the user_choice due to another method in this same class
        if isinstance(self.CURRENTLY_CARD, WildCard):
            self.CURRENTLY_CARD.user_choice = self.CURRENTLY_CARD.color

        return self.CURRENTLY_CARD

    def if_card_on_deck(self, card):
        return card in self.uno_deck.cards
