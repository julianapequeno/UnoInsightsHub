import random
from abc import ABC, abstractmethod

from src.CircularVector import CircularVector

#abstract class that have only abstract methods -> INTERFACE in python
class Behavior(ABC):
    @abstractmethod
    def execute(machine,players:CircularVector):
        pass

class BlockNextPlayer(Behavior):
    def execute(machine,players):
        machine.INDEX_WHO_IS_PLAYING += 1

class Reverse(Behavior):
    def execute(machine,players):     
        ##getting the last player's position on vector
        currently_player_name = players.vector[machine.INDEX_WHO_IS_PLAYING%len(players)].get_player().name.split()
        currently_player_number = int(currently_player_name[1])
        
        ##reversing vector
        players.vector.reverse()
        
        #updating vector by currently player index
        machine.INDEX_WHO_IS_PLAYING = players.get_vector_of_numbers().index(currently_player_number)
        
class DrawTwoCards(Behavior):
    def execute(machine,players):   
        if len(machine.uno_deck.cards) < 2: 
            machine.refuel_deck()
         
        new_cards = [machine.take_new_card_from_deck() for i in range(0,2)]
        
        for card in new_cards:
            players.get_ia_player_by_index(machine.INDEX_WHO_IS_PLAYING+1).get_player().add_cart_to_list(card)
        
class DrawFourCards(Behavior):
    def execute(machine,players):        
        if len(machine.uno_deck.cards) < 4:
            machine.refuel_deck()

        new_cards = [machine.take_new_card_from_deck() for i in range(0,4)]
        
        for card in new_cards:
                players.get_ia_player_by_index(machine.INDEX_WHO_IS_PLAYING+1).get_player().add_cart_to_list(card)
    
class ChangeColor(Behavior):
    def execute(machine,players):
        new_color = random.sample(machine.uno_deck.colors,1)
        machine.CURRENTLY_CARD.color = new_color[0]