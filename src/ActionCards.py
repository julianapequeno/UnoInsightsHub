import random

class ActionCards:
    
    def block_card_action(self, index):
        return (index + 1)
    
    def reverse_card_action(self,players,index):
        ##getting the last player's position on vetor
        currently_player_name = players.vetor[index%4].me_player.name.split()
        currently_player_number = int(currently_player_name[1])
        
        ##reversing vetor
        players.vetor.reverse()
        
        #updating vector by currently player index
        index = players.get_vector_of_numbers().index(currently_player_number)
        return index
        #for ia_player in players.vetor:
         #   name = ia_player.me_player.name.split()
          #  if int(name[1]) == currently_player_number:
           #     index = i
            #i+=1 
    
    def choose_a_new_color_card_action(self,uno_deck):
        new_color = random.sample(uno_deck.colors,1)
        return new_color[0]
    
    def seven_action_card(self,players):
        probability_of_saying_something = 20
        
        result = random.randint(1,101)
        
        if result <= probability_of_saying_something: #someone said something
            who_said = random.sample(players.vetor,1)
            new_card = self.take_new_card_from_deck()
            who_said[0].draw_from_deck(new_card) #puxa uma carta
            print("Someone falou no 7!")       
        
    def zero_action_card(self,players, index):
        q_cards_of_others_players = []
        player_q_cards = len(players.vetor[index%4].me_player.my_cards)
        
        for i in range(0, len(players)):
            q_cards_of_others_players.append(players.get_player_by_index(i))
        
        good_for_exchange = [ i  for i in q_cards_of_others_players if len(i.me_player.my_cards) < player_q_cards]

        if len(good_for_exchange) != 0:
            prob = random.randint(1,101)
            if prob >= 40: #60% de probabilidade de trocar
                #exchange!
                change_hand_with = random.sample(good_for_exchange,1)
                aux = change_hand_with[0].me_player.my_cards

                change_hand_with[0].me_player.my_cards = players.get_player_by_index(index%4).me_player.my_cards
                players.vetor[index%4].me_player.my_cards = aux

        else:
            #o jogador consegue ver as cartas do outro
            pass
       