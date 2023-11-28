from src.simulation_main.UnoSimulation import UnoSimulation, SimulationInputData
from tests.SimulationInputTest import SimulationInputTest
from src.controller.Machine import Machine
from src.bots.PlayerStrategy1 import PlayerStrategy1
from src.utils.CircularVector import CircularVector
from src.entity.ActionCards import ActionCard


class SimulationGenerator:
    def __init__(self, number_of_players, n_cards_fixed_input: list):
        self.PLAYERS = self.generating_players()
        self.number_of_players = number_of_players
        self.bot = Machine()
        self.number_of_fixed_cards_input = n_cards_fixed_input
        self.CARDS_INPUT_SIMULATION = SimulationInputTest(
            self.number_of_players, self.bot
        )

    def generating_players(self) -> CircularVector:
        PLAYERS = CircularVector(4)

        for i in range(0, 4):
            player_name = "Player " + str(i)
            ia_player = PlayerStrategy1(player_name)
            PLAYERS.add(ia_player)
        return PLAYERS

    def update_for_new_simulation(self):
        if self.number_of_fixed_cards_input:
            for i in range(0, self.number_of_players):
                if i not in self.number_of_fixed_cards_input:
                    new_sample_cards = self.generating_aleatory_samples_players_cards(
                        1)
                    self.initial_players_cards[i] = new_sample_cards[0]
        else:
            self.initial_players_cards = self.generating_aleatory_samples_players_cards(
                self.number_of_players
            )

    def generate_new_simulation_input_sample(self):
        self.initial_players_cards = self.generating_aleatory_samples_players_cards(
            self.number_of_players
        )

    def generating_uno_simulation(self):
        simulation_data = SimulationInputData(
            self.bot,
            self.PLAYERS,
            self.number_of_players,
        )
        return UnoSimulation(simulation_data)

    def generating_aleatory_samples_players_cards(self, number_of_samples):
        return self.CARDS_INPUT_SIMULATION.aleatory_sample_player_cards(
            number_of_samples
        )

    def get_game_first_card(self):
        self.FIRST_CARD = self.CARDS_INPUT_SIMULATION.get_game_first_card()
        return self.FIRST_CARD

    def verify_action_card(self, player_hand) -> tuple:
        action_card_count = 0
        normal_card_count = 0

        for card in player_hand:
            if isinstance(card, ActionCard):
                action_card_count += 1
            else:
                normal_card_count += 1
        return (action_card_count, normal_card_count)

    def get_players_initial_cards(self):
        return self.initial_players_cards

    def calculating_probability_of_player_having_card_to_throw_on_hand(
        self, player_cards
    ):
        count = 0
        for card in player_cards:
            if card.rank == self.FIRST_CARD.rank or card.color == self.FIRST_CARD.color:
                count += 1
        return count
