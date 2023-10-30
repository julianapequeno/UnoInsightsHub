#class made for testing the entries of players hands
class SimulationInputTest:
    def __init__(self, n_players, machine):
        self.n_players = n_players
        self.bot = machine
        
    def test_one_aleatory_sample_players_hands(self):
        hands_test_one = []
        for _ in range(0,self.n_players):
            hand = self.bot.get_player_first_hand()
            hands_test_one.append(hand)
        return hands_test_one
    
    def get_game_first_card(self):
        return self.bot.get_game_first_card()
        