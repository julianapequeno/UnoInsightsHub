from src.entity.CardsBehaviors import Behavior
from src.utils.CircularVector import CircularVector
import random
import logging

"""
This module represents extras UNO action cards.
"""

"""class of Number Nine action card, the one when everyone hits the table
"""


class NumberNineHitTable(Behavior):
    def execute(machine, players: CircularVector):
        vector_of_players = players.vector.copy()
        random.shuffle(vector_of_players)

        player_who_hit_table_last_time = random.choice(vector_of_players)

        player_who_hit_table_last_time.get_player().add_cart_to_list(
            machine.take_new_card_from_deck())

        logging.debug(
            f'{player_who_hit_table_last_time.get_player_name()} hit the table last (+1)')


class NumberSevenEverybodyOnMute(Behavior):
    def execute(machine, players: CircularVector):
        for player in players.vector:
            number = random.random()
            if number < 0.2:
                player.get_player().add_cart_to_list(
                    machine.take_new_card_from_deck())

                logging.debug(
                    f'{player.get_player_name()} spoke during a silence card (+1)')
