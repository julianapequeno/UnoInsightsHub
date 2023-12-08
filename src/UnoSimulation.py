from dataclasses import dataclass
from src.entity.Card import Card
from src.utils.CircularVector import CircularVector
from src.controller.Machine import Machine
import copy
import logging


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
    is_analysing_data: bool


class UnoSimulation:
    STATUS_CAN_PLAY = False
    INITIAL_PLAYERS_CARDS = []

    logging.basicConfig(
        level=logging.DEBUG,
        filemode='w',
        filename="logs\loggingfile.log"
    )

    def __init__(self, input: SimulationInputData):
        self.bot = input.bot
        self.number_of_players = input.number_of_players
        self.IS_ANALYSING_DATA = input.is_analysing_data
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

    def initialize_players_with_cards(self, player_cards):
        if self.IS_ANALYSING_DATA and (player_cards is not None):
            self.INITIAL_PLAYERS_CARDS = player_cards[:]

        i = 0
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            if self.IS_ANALYSING_DATA and (player_cards is not None):
                ia_player.player.setcards(player_cards[i])
            else:
                self.generate_player_cards(ia_player)
            i += 1

    def generate_player_cards(self, ia_player):
        cards = self.bot.get_player_first_hand()
        ia_player.player.setcards(cards)
        self.INITIAL_PLAYERS_CARDS.append(
            list(map(lambda x: str(x), cards)))

    def reset_simulation(self):
        for ia_player in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
            ia_player.reset_ia_player()

        self.bot.reset_machine(self.IS_ANALYSING_DATA,
                               self.INITIAL_PLAYERS_CARDS.copy())

        if not self.IS_ANALYSING_DATA:
            self.INITIAL_PLAYERS_CARDS = []

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

    def passing_info_about_next_player_to_the_currently(self):
        next_player_number_of_cards = len(
            self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(
                self.bot.INDEX_WHO_IS_PLAYING + 1
            )
            .get_player_cards()
        )
        self.CURRENTLY_PLAYER.vision_awareness_about_next_player_number_of_card(
            next_player_number_of_cards)

    def round(
        self, first_card=None, input_players_cards_new_round=None
    ) -> SimulationOutputData:
        self.first_card = first_card
        logging.info('Starting new round...')
        logging.info(f'>> Number of players {self.number_of_players} players ')
        logging.info(f'IS_ANALYSING_DATA = {self.IS_ANALYSING_DATA}')

        if self.STATUS_CAN_PLAY:
            self.initialize_players_with_cards(input_players_cards_new_round)

            for p in self.IA_PLAYERS_CIRCULAR_VECTOR.vector:
                logging.info(
                    f'>> {p.get_player_name()} initial cards[{len(p.get_player_cards())}c]: {list(map(lambda x: str(x),p.get_player_cards()))}')

            self.bot.shuffle_cards()
            self.initialize_game_with_first_card(first_card)

            while True:
                self.update_currently_player()
                self.bot.check_if_deck_is_empty_and_refuel_deck()

                self.passing_info_about_next_player_to_the_currently()

                card_thrown = self.CURRENTLY_PLAYER.move()
                player_passed_their_turn = card_thrown == None

                if not player_passed_their_turn:
                    self.CARD_ON_THE_TABLE = card_thrown

                    logging.info(
                        f'{self.CURRENTLY_PLAYER.get_player_name()}[{len(self.CURRENTLY_PLAYER.get_player_cards())+1}c] > {card_thrown}')

                    if self.player_has_won():

                        logging.info(
                            f'{self.CURRENTLY_PLAYER.get_player_name()} has won')

                        name = self.CURRENTLY_PLAYER.get_player_name()
                        return self.simulation_data(name)

                    card_thrown.execute_move(
                        self.bot, self.IA_PLAYERS_CIRCULAR_VECTOR)
                else:
                    logging.info(
                        f'{self.CURRENTLY_PLAYER.get_player_name()}[{len(self.CURRENTLY_PLAYER.get_player_cards())}c] has passed their turn.')
                self.bot.INDEX_WHO_IS_PLAYING += 1
        else:
            return None

    def player_has_won(self):
        return self.bot.winner(self.CURRENTLY_PLAYER.get_player_cards())

    def simulation_data(self, name):
        if self.IS_ANALYSING_DATA:
            init_cards = []
            for hand in self.INITIAL_PLAYERS_CARDS:
                init_cards.append(
                    list(map(lambda x: str(x), hand)))

            out = SimulationOutputData(
                name, init_cards, self.first_card)
        else:
            out = SimulationOutputData(
                name, self.INITIAL_PLAYERS_CARDS, self.first_card)
        self.reset_simulation()
        return out

    def print_cant_run_UNO_error_message(self):
        print(
            "Sorry. The number of players is either exceding the limit or under the minimum number"
        )
