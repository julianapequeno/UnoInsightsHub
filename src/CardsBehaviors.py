import random
from abc import ABC, abstractmethod

#abstract class that have only abstract methods -> INTERFACE in python
class Behavior(ABC):
    @abstractmethod
    def execute(machine):
        pass

class BlockNextPlayer(Behavior):
    def execute(machine):
        machine.INDEX_WHO_IS_PLAYING += 1

class Reverse(Behavior):
    def execute(machine):     
        ##getting the last player's position on vetor
        currently_player_name = machine.players.vetor[machine.INDEX_WHO_IS_PLAYING%len(machine.players)].get_player().name.split()
        currently_player_number = int(currently_player_name[1])
        
        ##reversing vetor
        machine.players.vetor.reverse()
        
        #updating vector by currently player index
        machine.INDEX_WHO_IS_PLAYING = machine.players.get_vector_of_numbers().index(currently_player_number)
        
class DrawTwoCards(Behavior):
    def execute(machine):   
        if len(machine.uno_deck.cards) < 2: #É RESPONSA DO MACHINE
            machine.refuel_deck()
         
        new_cards = [machine.take_new_card_from_deck() for i in range(0,2)]
        
        for card in new_cards:
            machine.players.get_ia_player_by_index(machine.INDEX_WHO_IS_PLAYING+1).get_player().take_a_new_card(card)
        
class DrawFourCards(Behavior):
    def execute(machine):        
        if len(machine.uno_deck.cards) < 4:
            machine.refuel_deck()
         
        new_cards = [machine.take_new_card_from_deck() for i in range(0,4)]
        
        for card in new_cards:
                machine.players.get_ia_player_by_index(machine.INDEX_WHO_IS_PLAYING+1).get_player().take_a_new_card(card)
        
class ChangeColor(Behavior):
    def execute(machine):        
        new_color = random.sample(machine.uno_deck.colors,1)
        machine.CURRENTLY_CARD.color = new_color[0]