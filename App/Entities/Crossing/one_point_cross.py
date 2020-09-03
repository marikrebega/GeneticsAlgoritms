import random
from App.Entities.Crossing.crossing import Crossing


class OnePointCross(Crossing):
    def __init__(self, father):
        super().__init__()
        self.new_generation = self.__new_generation(father)

    def __init_child(self, crossing_point):
        for j in range(crossing_point):
            self.child1 += self.mom[j]
            self.child2 += self.dad[j]
        for j in range(crossing_point, len(self.dad)):
            self.child1 += self.dad[j]
            self.child2 += self.mom[j]

    def __new_generation(self, father):
        crossing_point = random.randrange(1, 6)
        print("Cross Point: ", crossing_point)
        binary_population = {}
        new_generation = []
        temporary_generation = []
        for i in range(len(father)):
            binary_population[i] = bin(father[i])
        for i in range(0, len(binary_population), 2):
            self.child1 = ""
            self.child2 = ""
            if binary_population[i][0:1] == "-" and binary_population[i + 1][0:1] == "-":
                self.dad = binary_population[i][3:].zfill(6)
                self.mom = binary_population[i + 1][3:].zfill(6)
                self.__init_child(crossing_point)
                self.mutate_person()
                self.dad = "-0b" + self.dad
                self.mom = "-0b" + self.mom
                self.child1 = "-0b" + self.child1
                self.child2 = "-0b" + self.child2
                self.append_generation(temporary_generation)
            elif binary_population[i][0:1] == "-" and binary_population[i + 1][0:1] != "-":
                self.dad = binary_population[i][3:].zfill(6)
                self.mom = binary_population[i + 1][2:].zfill(6)
                self.__init_child(crossing_point)
                self.mutate_person()
                self.dad = "-0b" + self.dad
                self.mom = "0b" + self.mom
                self.child1 = "0b" + self.child1
                self.child2 = "-0b" + self.child2
                self.append_generation(temporary_generation)
            elif binary_population[i][0:1] != "-" and binary_population[i + 1][0:1] == "-":
                self.dad = binary_population[i][2:].zfill(6)
                self.mom = binary_population[i + 1][3:].zfill(6)
                self.__init_child(crossing_point)
                self.mutate_person()
                self.dad = "0b" + self.dad
                self.mom = "-0b" + self.mom
                self.child1 = "-0b" + self.child1
                self.child2 = "0b" + self.child2
                self.append_generation(temporary_generation)
            else:
                self.dad = binary_population[i][2:].zfill(6)
                self.mom = binary_population[i + 1][2:].zfill(6)
                self.__init_child(crossing_point)
                self.mutate_person()
                self.dad = "0b" + self.dad
                self.mom = "0b" + self.mom
                self.child1 = "0b" + self.child1
                self.child2 = "0b" + self.child2
                self.append_generation(temporary_generation)
        for i in range(len(temporary_generation)):
            new_generation.append(int(temporary_generation[i], 2))
        return new_generation
