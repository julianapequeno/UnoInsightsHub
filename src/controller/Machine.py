from src.entity.Card import Card
from src.entity.UnoDeck import UnoDeck
from src.entity.WildCard import WildCard
from src.entity.CardsBehaviors import ChangeColor


class Machine:  # controller
    def __init__(self):
        self.uno_deck = UnoDeck()
        self.CURRENTLY_CARD: Card
        self.INDEX_WHO_IS_PLAYING = 0

    def reset_machine(self, players_input_fixed):
        self.uno_deck.reset(players_input_fixed)
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
        if isinstance(self.CURRENTLY_CARD, WildCard) and isinstance(
            self.CURRENTLY_CARD.behavior, ChangeColor
        ):
            if (card.rank == self.CURRENTLY_CARD.rank) or (
                card.user_choice == self.CURRENTLY_CARD.color
            ):
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
        # draw a brand new card from deck
        self.CURRENTLY_CARD = self.take_new_card_from_deck()
        return self.CURRENTLY_CARD

    def if_card_on_deck(self, card):
        return card in self.uno_deck.cards
