from dataclasses import dataclass
from data_analysis.SimulationGenerator import SimulationGenerator
import pandas as pd


@dataclass
class UNO_MODE:
    HAVE_A_FIXED_INITIAL_CARD: bool  # = False
    FIXED_INDEX_PLAYERS_CARDS: list  # = []
    NUMBER_OF_PLAYERS: int  # = 4
    NUMBER_OF_SIMULATIONS: int  # = 500


class SanityTest:

    def __init__(self, input: UNO_MODE):
        self.probabilities_list = []
        self.HAVE_A_FIXED_INITIAL_CARD = input.HAVE_A_FIXED_INITIAL_CARD
        self.FIXED_INDEX_PLAYERS_CARDS = input.FIXED_INDEX_PLAYERS_CARDS
        self.NUMBER_OF_PLAYERS = input.NUMBER_OF_PLAYERS
        self.NUMBER_OF_SIMULATIONS = input.NUMBER_OF_SIMULATIONS
        self.ganhadores = []

    def create_simulation(self):
        self.simulation = SimulationGenerator(
            number_of_players=self.NUMBER_OF_PLAYERS, n_cards_fixed_input=self.FIXED_INDEX_PLAYERS_CARDS)
        self.simulation.generate_new_simulation_input_sample()
        self.UNO = self.simulation.generating_uno_simulation()

    def check_fixed_card(self):
        if self.HAVE_A_FIXED_INITIAL_CARD:
            self.FIXED_INITIAL_CARD = self.simulation.get_game_first_card()
        else:
            self.FIXED_INITIAL_CARD = None

    def generate_simulation_n_times(self):
        self.ganhadores.clear()
        for j in range(0, self.NUMBER_OF_SIMULATIONS):
            retorno = self.UNO.round(
                self.FIXED_INITIAL_CARD, self.simulation.initial_players_cards)

            if not self.FIXED_INITIAL_CARD:
                self.simulation.FIRST_CARD = retorno.first_card

            self.ganhadores.append(retorno.winner)
            self.simulation.update_for_new_simulation()

        player_0_won = self.ganhadores.count('Player 0')
        prob_ganhar = player_0_won/self.NUMBER_OF_SIMULATIONS
        self.probabilities_list.append(prob_ganhar)

    def get_probabilities_list(self):
        return self.probabilities_list

    def reset_probabilities_list(self):
        self.probabilities_list = []
