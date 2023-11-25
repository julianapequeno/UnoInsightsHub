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
            self.print_simulation_scrip()

            self.bot.shuffle_cards()
            self.initialize_game_with_first_card()

            self.print_game_beggining(self.CARD_ON_THE_TABLE)
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
                    self.print_card_thrown(card_thrown)
                    self.check_if_it_is_uno()

                    if self.player_has_won():
                        name = self.CURRENTLY_PLAYER.get_player_name()
                        return self.simulation_data(name)

                    card_thrown.execute_move(
                        self.bot, self.IA_PLAYERS_CIRCULAR_VECTOR)
                else:
                    self.print_player_passed_their_turn()

                self.bot.INDEX_WHO_IS_PLAYING += 1
        else:
            self.print_cant_run_UNO_error_message()
            return None

    def player_has_won(self):
        if self.bot.winner(self.CURRENTLY_PLAYER.get_player_cards()):
            print(self.CURRENTLY_PLAYER.get_player_name()+' won the game')
            return True
        else:
            return False

    def simulation_data(self, name):
        out = SimulationOutputData(
            name, self.INITIAL_PLAYERS_CARDS, self.first_card)
        self.reset_simulation()
        return out

    def print_player_passed_their_turn(self):
        print(self.CURRENTLY_PLAYER.get_player_name()+" has passed their turn")

    def print_simulation_scrip(self):
        print(">>>>>>>>> Launching UNO")
        print(f"Simulating with {self.number_of_players} players")
        print("* PLAYERS INITIAL CARDS: ")

        print(self.IA_PLAYERS_CIRCULAR_VECTOR)
        for i in range(0, self.number_of_players):
            print(">>>> Player ", i)
            for card in self.IA_PLAYERS_CIRCULAR_VECTOR.get_ia_player_by_index(i).get_player_cards():
                print(f"Card [{card.rank},{card.color}]")

    def print_game_beggining(self, card):
        print(">> INITIAL CARD: ", str(card))
        print(">>>>>>>>>>>>>>>>> GAME BEGINS")

    def print_card_thrown(self, card):
        print('> ', self.CURRENTLY_PLAYER.get_player_name(),
              ' has thrown ', self.CARD_ON_THE_TABLE)

    def print_game_beggining(self, card):
        print(">> INITIAL CARD: ", str(card))
        print(">>>>>>>>>>>>>>>>> GAME BEGINS")

    def check_if_it_is_uno(self):
        if (self.bot.is_UNO(self.CURRENTLY_PLAYER.get_player_cards())):
            print("UNO! - "+self.CURRENTLY_PLAYER.get_player_name())

    def print_cant_run_UNO_error_message(self):
        print(
            "Sorry. The number of players is either exceding the limit or under the minimum number"
        )
