import random 
from UnoDeck import UnoDeck 
from VetorCircular import VetorCircular
from Player import Player

class Bot:
    def __init__(self,n_players):
        self.uno = UnoDeck()
        self.players = VetorCircular(n_players)
        self.n_players = n_players

    #Actions made with CARDS
    def shuffle_cards(self):
        random.shuffle(self.uno.cards)

    def add_to_cards_main_pile(self,card):
        #adiciona a nova carta à pilha de descarte
        self.uno.discart_a_card(card)
    
    def draw_a_card_from_deck(self): #to draw a card #puxar da pilha
        return self.uno.take_new_card_from_deck()
    
    def players_initialization_with_random_cards(self): # Escolhe 7 cartas aleatórias para cada jogador e as retira da lista original
        for j in range(0,self.n_players):
            player_cards = self.uno.draw_new_hand()
            self.deleting_cards_from_main_deck(player_cards)
            self.players.adicionar(Player("Player "+str(j+1),player_cards))
        return self.players
    
    def deleting_cards_from_main_deck(self,selected_cards):
        for card in selected_cards:
            self.uno.delete_card_from_deck(card)

    # Actions made for and with players interventions! 
    def initialize_players(self):
        self.players = self.players_initialization_with_random_cards() #a ordem de jogo está na lista, realize swaps quando as cartas alterarem!!


    def start_player_turn(self,player):
        self.whoIsPlaying = player
        #guarda em uma lista todas as possibilidades de jogadas, cartas
        list_of_possible_throws = self.possible_throws(player)

        if(list_of_possible_throws == 0): #user takes another card
            new_card = self.uno.take_new_card_from_deck()
            player.get_new_card(new_card)
            if(self.card_can_be_throw(new_card)):
                player.throw_card(new_card)
                self.add_to_cards_main_pile(new_card)

        else:  
            self.currently_card = random.sample(list_of_possible_throws,1) #pega uma aleatória entre as possíveis
            self.add_to_cards_main_pile(self.currently_card) #joga na mesa

            player.throw_card(self.currently_card[0]) # apaga da mao do usuário
            print(player.get_cards())
            print(self.currently_card)
            # for pos_card in possible_throws:
                # if pos_card[0] == '+': #verifica se é melhor soltar o +2 agora :) haha
                # should_throw_add = self.check_quantity_of_next_player()
                # if(should_throw_add):
                    # return pos_card
        if(player.get_cards() == 1):
            print("UNO!")


    def possible_throws(self,player): #retorna a lista de possíveis jogadas
        possible_throws = []
        for play_card in player.get_cards():
            if(self.card_can_be_throw(play_card)):
                possible_throws.append(play_card)
        return possible_throws
    
    def card_can_be_throw(self,card): #verifica se a carta pode ser jogada
        if (card[1] == self.currently_card[0][1]) or (card[0] == self.currently_card[0][0]):
            return True
        return False
    

    def rodada(self):
        self.index_who_is_playing = 0
        self.shuffle_cards() #embaralha
        self.initialize_players() #inicializa os jogadores com suas cartas
        self.currently_card =  self.draw_a_card_from_deck()#initial card
        print("ON THE TABLE: ", self.currently_card)
        while(True):
            self.who_is_currently_playing = self.players.get_player_by_index(self.index_who_is_playing)
            self.start_player_turn(self.who_is_currently_playing) 
            self.index_who_is_playing += 1
            if(self.who_is_currently_playing.get_cards() == 0):
                print(self.who_is_currently_playing.get_name()," ganhou!")
                break


if __name__ == '__main__':
  bot = Bot(4)
  bot.rodada()