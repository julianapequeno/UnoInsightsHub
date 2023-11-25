from dataclasses import dataclass
from entity.Card import Card
from utils.CircularVector import CircularVector
from controller.Machine import Machine
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


class UnoSimulation:
    STATUS_CAN_PLAY = False
    INITIAL_PLAYERS_CARDS = []

    def __init__(self, input: SimulationInputData):
        self.bot = input.bot
        self.number_of_players = input.number_of_players
        self.verify_initial_parameters()

        if self.STATUS_CAN_PLAY:
            self.IA_PLAYERS_CIRCULAR_VECTOR = input.round_players
            self.insert_bot_into_players()

    def verify_initial_parameters(self):
        self.STATUS_CAN_PLAY = self.bot.can_this_number_of_players_play_uno(
            self.number_of_players
        )

    def insert_bot_into_players(self):
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            ia_player.insert_uno_machine(self.bot)

    def initialize_players_with_cards(self):
        i = 0
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            cards = self.bot.get_player_first_hand()
            ia_player.player.setcards(cards)
            self.INITIAL_PLAYERS_CARDS.append(
                list(map(lambda x: (str(x)), cards)))
            i += 1

    def reset_simulation(self):
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            ia_player.reset_ia_player()

        self.bot.reset_machine()

        self.CARD_ON_THE_TABLE = None
        self.CURRENTLY_PLAYER = []

    def initialize_game_with_first_card(self):
        self.CARD_ON_THE_TABLE = self.bot.get_game_first_card()
        self.first_card = copy.copy(self.CARD_ON_THE_TABLE)

    def update_currently_player(self):
        self.CURRENTLY_PLAYER = self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(
            self.bot.INDEX_WHO_IS_PLAYING
        )

    def round(self) -> SimulationOutputData:
        if self.STATUS_CAN_PLAY:
            self.initialize_players_with_cards()
            self.bot.shuffle_cards()

            while True:
                self.update_currently_player()
                self.bot.check_if_deck_is_empty_and_refuel_deck()

                # create a method called awareness in ia_player class
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

                    if self.player_has_won():
                        name = self.CURRENTLY_PLAYER.get_player_name()
                        return self.simulation_data(name)

                    card_thrown.execute_move(
                        self.bot, self.IA_PLAYERS_CIRCULAR_VECTOR)

                self.bot.INDEX_WHO_IS_PLAYING += 1
        else:
            return None

    def player_has_won(self):
        return self.bot.winner(self.CURRENTLY_PLAYER.get_player_cards())

    def simulation_data(self, name):
        out = SimulationOutputData(
            name, self.INITIAL_PLAYERS_CARDS, self.first_card)
        self.reset_simulation()
        return out

    def print_cant_run_UNO_error_message(self):
        print(
            "Sorry. The number of players is either exceding the limit or under the minimum number"
        )
