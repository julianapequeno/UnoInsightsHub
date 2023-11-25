import random
from abc import ABC, abstractmethod

from utils.CircularVector import CircularVector


# abstract class that have only abstract methods -> INTERFACE in python
class Behavior(ABC):
    @abstractmethod
    def execute(machine, players: CircularVector):
        pass


class BlockNextPlayer(Behavior):
    def execute(machine, players):
        machine.INDEX_WHO_IS_PLAYING += 1
        blocked_player = players.vector[machine.INDEX_WHO_IS_PLAYING % (
            len(players))]
        print('Reac: ', blocked_player.get_player_name(), ' was blocked')


class Reverse(Behavior):
    def execute(machine, players):
        # getting the last player's position on vector
        currently_player_name = (
            players.vector[machine.INDEX_WHO_IS_PLAYING % len(players)]
            .get_player()
            .name.split()
        )
        currently_player_number = int(currently_player_name[1])

        # reversing vector
        players.vector.reverse()

        # updating vector by currently player index
        machine.INDEX_WHO_IS_PLAYING = players.get_vector_of_numbers().index(
            currently_player_number
        )
        print('Reac: ', list(map(lambda x: x.get_player_name(), players.vector)))


class DrawTwoCards(Behavior):
    def execute(machine, players):
        if len(machine.uno_deck.cards) < 2:
            machine.refuel_deck()

        new_cards = [machine.take_new_card_from_deck() for i in range(0, 2)]

        next_player = players.get_ia_player_by_index(
            machine.INDEX_WHO_IS_PLAYING + 1
        ).get_player()

        old_cards_length = len(next_player.cards)

        for card in new_cards:
            next_player.add_cart_to_list(card)

        print('Reac: ', next_player.name,
              ' pulled from deck : ', old_cards_length, ' >>> ', len(next_player.cards), ' cards (+2)')


class DrawFourCards(Behavior):
    def execute(machine, players):
        if len(machine.uno_deck.cards) < 4:
            machine.refuel_deck()

        new_cards = [machine.take_new_card_from_deck() for i in range(0, 4)]

        next_player = players.get_ia_player_by_index(
            machine.INDEX_WHO_IS_PLAYING + 1
        ).get_player()

        old_cards_length = len(next_player.cards)

        for card in new_cards:
            next_player.add_cart_to_list(card)

        print('Reac: ', next_player.name,
              ' pulled from deck : ', old_cards_length, ' >>> ', len(next_player.cards), ' cards (+4)')


class ChangeColor(Behavior):
    def execute(machine, players):
        currently_player = players.vector[machine.INDEX_WHO_IS_PLAYING % (
            len(players))]
        new_color = random.sample(machine.uno_deck.colors, 1)
        machine.CURRENTLY_CARD.user_choice = new_color[0]

        print('React: ', currently_player.get_player_name(),
              ' has chosen ', new_color[0])
