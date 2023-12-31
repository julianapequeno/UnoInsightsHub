# imported


class CircularVector:
    def __init__(self, size):
        self.size = size
        self.vector = [None] * size
        self.begin = 0  # Índice de início
        self.end = 0  # Índice de end
        self.currently_size = 0  # Tamnho atual do vector

    def add(self, element):
        if self.currently_size < self.size:
            self.vector[self.end] = element
            self.end = (self.end + 1) % self.size
            self.currently_size += 1

    def remove(self):
        if self.currently_size > 0:
            removed_element = self.vector[self.begin]
            self.begin = (self.begin + 1) % self.size
            self.currently_size -= 1
            return removed_element

    def __str__(self):
        return f"{self.vector}"

    def __len__(self):
        return len(self.vector)

    def get_ia_player_by_index(self, pos):
        return self.vector[pos % self.size]

    def set_new_vetor(self, vector):
        self.vector = vector

    def get_vector(self):
        vec = []
        for el in self.vector:
            vec.append(el.player.name)
        return vec

    def get_vector_of_numbers(self):
        vec = []
        for el in self.vector:
            list_vect = el.player.name.split()
            numb = int(list_vect[1])
            vec.append(numb)
        return vec
