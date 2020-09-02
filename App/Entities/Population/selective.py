import random
from .population import Population


class Selective(Population):
    def __init__(self):
        super().__init__()
        self.generations = self.make_gen_selective()

    def make_gen_selective(self):
        generations = []
        length = 8
        for i in range(length):
            generations.append(random.randrange(self.get_min(), self.get_max()))
        return generations
