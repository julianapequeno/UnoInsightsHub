import random

class IAPlayer:
    def __init__(self,player,ia_cards):
        self.player = player
        self.ia_cards = ia_cards
        self.initialize_player_cards()
        
    def initialize_player_cards(self):
        self.player.player_cards = self.ia_cards.entrega_mao_do_jogador()
    
    def throw_cards_into_pile(self,card):
        #adiciona a nova carta à pilha de descarte
        self.ia_cards.discart_a_card(card)

    def draw_from_deck(self):
        new_card = self.ia_cards.take_new_card_from_deck()
        self.player.get_new_card(new_card)
        
    def player_throw_card_action(self,card):
        self.player.throw_card(card)
        self.ia_cards.discart_a_card(card)

        list_card_action = self.ia_cards.uno.action_cards(card)
        if list_card_action[0] == 'C':
            new_color = list_card_action[1]
            card = self.ia_cards.uno.uno(card[0],new_color)
        return list_card_action        
    
    def start_player_turn(self) :
        if not self.ia_cards.deck_is_null():

            list_of_possible_throws = self.possible_throws(self.player)
            if(len(list_of_possible_throws) == 0): #user takes another card
                new_card = self.ia_cards.take_new_card_from_deck()
                self.player.get_new_card(new_card)

                if(self.card_can_be_throw(new_card)):
                    list_action_or_not_card = self.player_throw_card_action(new_card)

            else:  
                aleatory_card = random.sample(list_of_possible_throws,1) #pega uma aleatória entre as possíveis
                list_action_or_not_card = self.player_throw_card_action(aleatory_card[0])
                
                ## ALGORITMO PARA MELHOR ESCOLHA DAS CARTAS A SEREM JOGADAS
                # for pos_card in possible_throws:
                    # if pos_card[0] == '+': #verifica se é melhor soltar o +2 agora :) haha
                    # should_throw_add = self.check_quantity_of_next_player()
                    # if(should_throw_add):
                        # return pos_card
            if self.is_UNO():
                print("UNO")
                return list("U")
            elif self.winner():
               # print("GANHOU")
                return list("G")
        else:
            print("REABASTECENDO O DECK")
            self.ia_cards.refuel_deck()
        return list_action_or_not_card
    
    def is_UNO(self):
        if(len(self.player.get_cards()) == 1):
            return True
        else:
            return False     
    def winner(self):
        if(len(self.player.get_cards()) == 0):
            return True
        else:
            return False
    
    def possible_throws(self,player): #retorna a lista de possíveis jogadas
        possible_throws = []
        for play_card in player.get_cards():
            if(self.card_can_be_throw(play_card)):
                possible_throws.append(play_card)
        return possible_throws
    
    def card_can_be_throw(self,card): #verifica se a carta pode ser jogada
        if (card[1] == self.ia_cards.currently_card[0][1]) or (card[0] == self.ia_cards.currently_card[0][0]):
            return True
        return False