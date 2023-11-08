from dataclasses import dataclass
from src.entity.Card import Card
from src.utils.CircularVector import CircularVector
from src.controller.Machine import Machine
import copy


@dataclass
class SimulationOutputData:
    winner: str
    first_players_hands: list[list[str]]
    first_card: Card


@dataclass
class SimulationInputData:
    bot: Machine
    round_players: CircularVector
    number_of_players: int
    players_cards: list[list[Card]]


class UnoSimulation:
    STATUS_CAN_PLAY = False
    IS_ANALYSING_DATA = True
    INITIAL_PLAYERS_CARDS = []

    def __init__(self, input: SimulationInputData):
        self.bot = input.bot
        self.number_of_players = input.number_of_players
        self.verify_initial_parameters()

        if self.STATUS_CAN_PLAY:
            self.IA_PLAYERS_CIRCULAR_VECTOR = input.round_players
            self.INITIAL_PLAYERS_CARDS = input.players_cards[:]
            self.insert_bot_into_players()

    def verify_initial_parameters(self):
        self.STATUS_CAN_PLAY = self.bot.can_this_number_of_players_play_uno(
            self.number_of_players
        )

    def insert_bot_into_players(self):
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            ia_player.insert_uno_machine(self.bot)

    def initialize_players_with_cards(self, player_cards):
        i = 0
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            ia_player.player.setcards(player_cards[i])
            i += 1

    def reset_simulation(self):
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            ia_player.reset_ia_player()

        self.bot.reset_machine(self.INITIAL_PLAYERS_CARDS.copy())

        self.CARD_ON_THE_TABLE = None
        self.CURRENTLY_PLAYER = []

    def initialize_game_with_first_card(self, first_card):
        if first_card:
            if self.bot.if_card_on_deck(first_card):
                self.bot.delete_cards_from_deck(first_card)

            self.CARD_ON_THE_TABLE = first_card
            self.first_card = copy.copy(self.CARD_ON_THE_TABLE)
        else:
            self.CARD_ON_THE_TABLE = self.bot.get_game_first_card()
            self.first_card = copy.copy(self.CARD_ON_THE_TABLE)

    def update_currently_player(self):
        self.CURRENTLY_PLAYER = self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(
            self.bot.INDEX_WHO_IS_PLAYING
        )

    def round(
        self, first_card=None, input_players_cards_new_round=None
    ) -> SimulationOutputData:
        self.first_card = first_card
        self.initialize_game_with_first_card(first_card)

        if self.STATUS_CAN_PLAY:
            self.initialize_players_with_cards(input_players_cards_new_round)
            self.bot.shuffle_cards()

            while True:
                self.update_currently_player()
                self.bot.check_if_deck_is_empty_and_refuel_deck()

                ##
                next_player_number_of_cards = len(
                    self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(
                        self.bot.INDEX_WHO_IS_PLAYING + 1
                    )
                    .get_player()
                    .cards
                )
                self.CURRENTLY_PLAYER.get_other_players_number_of_cards(
                    next_player_number_of_cards
                )
                ##

                card_thrown = self.CURRENTLY_PLAYER.move()
                player_passed_their_turn = card_thrown == None

                if not player_passed_their_turn:
                    self.CARD_ON_THE_TABLE = card_thrown

                    if self.player_has_won():  # simulation
                        name = self.CURRENTLY_PLAYER.get_player_name()
                        return self.simulation_data(name, input_players_cards_new_round)

                    card_thrown.execute_move(self.bot, self.IA_PLAYERS_CIRCULAR_VECTOR)

                self.bot.INDEX_WHO_IS_PLAYING += 1
        else:
            return None

    def player_has_won(self):
        return self.bot.winner(self.CURRENTLY_PLAYER.get_player_cards())

    def simulation_data(self, name, input_players_cards_new_round):
        initial_hands = []
        for player_cards in input_players_cards_new_round:
            player_h = []
            for card in player_cards:
                player_h.append(str(card))
            initial_hands.append(player_h)

        out = SimulationOutputData(name, initial_hands, self.first_card)
        self.reset_simulation()
        return out

    def print_cant_run_UNO_error_message(self):
        print(
            "Sorry. The number of players is either exceding the limit or under the minimum number"
        )
