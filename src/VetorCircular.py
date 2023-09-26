#imported 

class VetorCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [None] * tamanho
        self.inicio = 0  # Índice de início
        self.fim = 0     # Índice de fim
        self.tamanho_atual = 0  # Tamanho atual do vetor

    def adicionar(self, elemento):
        if self.tamanho_atual < self.tamanho:
            self.vetor[self.fim] = elemento
            self.fim = (self.fim + 1) % self.tamanho
            self.tamanho_atual += 1
        else:
            print("O vetor está cheio. Remova elementos antes de adicionar mais.")

    def remover(self):
        if self.tamanho_atual > 0:
            elemento_removido = self.vetor[self.inicio]
            self.inicio = (self.inicio + 1) % self.tamanho
            self.tamanho_atual -= 1
            return elemento_removido
        else:
            print("O vetor está vazio. Adicione elementos antes de remover.")

    def __str__(self):
        return str(self.vetor)
    
    def __len__(self):
        return len(self.vetor)
    
    def get_player_by_index(self, pos):
        return self.vetor[pos % self.tamanho]
    
    def set_new_vetor(self, vetor):
        self.vetor = vetor
        
    def get_vector(self):
        vec = []
        for el in self.vetor:
            vec.append(el.me_player.name)
        return vec
    
    def get_vector_of_numbers(self):
        vec = []
        for el in self.vetor:
            list_vect = el.me_player.name.split()
            numb = int(list_vect[1])
            vec.append(numb)
        return vec