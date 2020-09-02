import random
from .selection import Selection


class Selective(Selection):
    def __init__(self):
        super().__init__()
        self.generations = self.make_gen_selective()

    def make_gen_selective(self):
        generations = []
        length = 8
        for i in range(length):
            generations.append(random.randrange(self.get_min(), self.get_max()))
        return generations
