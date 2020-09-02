from .selection import Selection


class Blanket(Selection):
    def __init__(self):
        super().__init__()
        self.generations = self.make_gen_blanket()

    def make_gen_blanket(self):
        generations = []
        for i in range(self.get_min(), self.get_max(), 1):
            generations.append(i)
        return generations
