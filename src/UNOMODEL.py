from UnoSimulation import UnoSimulation, SimulationInputData
from controller.Machine import Machine
from utils.CircularVector import CircularVector
from bots.IA_Player import IA_Player
from bots.PlayerStrategy1 import PlayerStrategy1


while (True):
    print('>>>>>>>>>>>>>>>> UnoInsightsHub | Model')
    print('Hi there! Here you can run the model itself, and observe the game as longs as the players play. I hope you enjoy!')
    print('> Please choose the configuration that you want: ')
    numberOfPlayers = int(input('Number of Players: '))

    while (True):
        print('> Choose a strategy: ')
        print('1. PlayerStrategy1 - with PRIORITY_TO_THROW_ACTION_CARD, verify other players number of cards')
        chosen = int(input())

        if chosen == 1:
            break

    print('loading....')

    break


MACHINE = Machine()
PLAYERS = CircularVector(numberOfPlayers)

for i in range(0, numberOfPlayers):
    player_name = 'Player '+str(i)

    match chosen:
        case 1:
            ia_player = PlayerStrategy1(player_name)
        case _:
            ia_player = IA_Player(player_name)

    PLAYERS.add(ia_player)

simulation_data = SimulationInputData(MACHINE, PLAYERS, numberOfPlayers)

uno = UnoSimulation(simulation_data)
uno.round()
