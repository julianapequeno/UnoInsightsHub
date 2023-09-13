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

    def player_throw_card_action(self,player,card):
        player.throw_card(card) #player joga a carta e essa é excluida de sua mão
        self.add_to_cards_main_pile(card) # a carta é adicionada a pilha de descarte
        self.currently_card = card # a carta de cima da pilha é a carta jogada agora
        
        # ALGORITMO QUE VERIFICA ON IMPACTO DAS CARTAS JOGADAS NO JOGO
        card_action = self.uno.action_cards(card)
        if(card[0] == 'X'): # BLOQUEIO
            print(player.get_name()," bloqueou o próximo jogador")
            self.index_who_is_playing = card_action(self.index_who_is_playing)
        elif(card[0] == 'R'): # REVERSO
            print(player.get_name()," jogou um reverse")
            card_action(self.players.vetor)
          #  for i in range(0, len(self.players.vetor)):
              #  print(self.players.get_player_by_index(i).get_name())
        elif(card[0] == '+' or card[0] == 'W'): #SOMA DOIS ou QUATRO
            print(player.get_name()," jogou um puxa dois ou puxa quatro")
            for new_card in card_action():
                self.players.get_player_by_index(self.index_who_is_playing+1).get_new_card(new_card)
                print(self.players.get_player_by_index(self.index_who_is_playing+1).get_name()," está agora com ",len(self.players.get_player_by_index(self.index_who_is_playing+1).get_cards()))
        elif(card[0] == 'C'): # ESCOLHA A COR
            print(player.get_name()," jogou um change color")
            new_color = card_action()
            card = self.uno.uno(card[0],new_color[0])
            print("A card coringa ",card)

    def deck_is_null(self):
        if len(self.uno.cards) == 0:
            return True
        else:
            return False

    def start_player_turn(self,player):
        if not self.deck_is_null():
            #guarda em uma lista todas as possibilidades de jogadas, cartas
            list_of_possible_throws = self.possible_throws(player)
            if(len(list_of_possible_throws) == 0): #user takes another card
                new_card = self.uno.take_new_card_from_deck()
                player.get_new_card(new_card)
                print(player.get_name()," puxou uma nova carta")
                if(self.card_can_be_throw(new_card)):
                    self.player_throw_card_action(player,new_card)
                    print(player.get_name()," jogou a nova carta")
            else:  
                aleatory_card = random.sample(list_of_possible_throws,1) #pega uma aleatória entre as possíveis
                self.player_throw_card_action(player,aleatory_card[0])
                print(player.get_name()," jogou uma carta")
                
                ## ALGORITMO PARA MELHOR ESCOLHA DAS CARTAS A SEREM JOGADAS
                # for pos_card in possible_throws:
                    # if pos_card[0] == '+': #verifica se é melhor soltar o +2 agora :) haha
                    # should_throw_add = self.check_quantity_of_next_player()
                    # if(should_throw_add):
                        # return pos_card

            if(len(player.get_cards()) == 1):
                print("UNO!")
                return "UNO"
        else:
            print("REABASTECENDO O DECK")
            self.uno.refuel_deck()
        return ""

    def possible_throws(self,player): #retorna a lista de possíveis jogadas
        possible_throws = []
        for play_card in player.get_cards():
            if(self.card_can_be_throw(play_card)):
                possible_throws.append(play_card)
        return possible_throws
    
    def card_can_be_throw(self,card): #verifica se a carta pode ser jogada
        if (card[1] == self.currently_card[1]) or (card[0] == self.currently_card[0]):
            return True
        return False

    def rodada(self):
        self.index_who_is_playing = 0
        self.shuffle_cards() #embaralha
        self.initialize_players() #inicializa os jogadores com suas cartas
        self.currently_card =  self.draw_a_card_from_deck()#initial card
        while(True):
            print("TEMOS ",str(len(self.uno.cards))," cartas ativas")
            print("ON THE TABLE: ", self.currently_card)
            self.who_is_currently_playing = self.players.get_player_by_index(self.index_who_is_playing)
            
            print(self.who_is_currently_playing.get_name()," is playing right now")
            if self.start_player_turn(self.who_is_currently_playing) == "UNO":
                print(self.who_is_currently_playing.get_name()," ganhou!")
                break
            print("Quantidade de cartas ",len(self.who_is_currently_playing.get_cards()))
            self.index_who_is_playing += 1

if __name__ == '__main__':
  bot = Bot(4)
  bot.rodada()