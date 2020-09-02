import random
from .selection import Selection


class Shotgun(Selection):

    def __init__(self):
        super().__init__()
        self.generations = self.make_gen_shotgun()

    def make_gen_shotgun(self):
        generations = []
        length = int(len(range(self.get_min(), self.get_max(), 1))/2)
        for i in range(length):
            generations.append(random.randrange(self.get_min(), self.get_max()))
        return generations
