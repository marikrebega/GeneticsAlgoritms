import random
from App.Entities.Crossing.crossing import Crossing


class TwoPointCross(Crossing):
    def __init__(self, father):
        super().__init__()
        self.new_generation = self.__new_generation(father)

    def __init_child(self, crossing_points):
        for j in range(crossing_points[0]):
            self.child1 += self.mom[j]
            self.child2 += self.dad[j]
        for j in range(crossing_points[0], crossing_points[1]):
            self.child1 += self.dad[j]
            self.child2 += self.mom[j]
        for j in range(crossing_points[1], len(self.dad)):
            self.child1 += self.mom[j]
            self.child2 += self.dad[j]

    def __new_generation(self, father):
        temporary_point_1 = random.randrange(1, 6)
        temporary_point_2 = random.randrange(1, 6)
        while temporary_point_1 == temporary_point_2:
            temporary_point_2 = random.randrange(1, 6)
        crossing_points = [temporary_point_1, temporary_point_2]
        crossing_points.sort()
        print("Cross Points: ", crossing_points)
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
                self.__init_child(crossing_points)
                self.mutate_person()
                self.dad = "-0b" + self.dad
                self.mom = "-0b" + self.mom
                self.child1 = "-0b" + self.child1
                self.child2 = "-0b" + self.child2
                self.append_generation(temporary_generation)
            elif binary_population[i][0:1] == "-" and binary_population[i + 1][0:1] != "-":
                self.dad = binary_population[i][3:].zfill(6)
                self.mom = binary_population[i + 1][2:].zfill(6)
                self.__init_child(crossing_points)
                self.mutate_person()
                self.dad = "-0b" + self.dad
                self.mom = "0b" + self.mom
                self.child1 = "0b" + self.child1
                self.child2 = "-0b" + self.child2
                self.append_generation(temporary_generation)
            elif binary_population[i][0:1] != "-" and binary_population[i + 1][0:1] == "-":
                self.dad = binary_population[i][2:].zfill(6)
                self.mom = binary_population[i + 1][3:].zfill(6)
                self.__init_child(crossing_points)
                self.mutate_person()
                self.dad = "0b" + self.dad
                self.mom = "-0b" + self.mom
                self.child1 = "-0b" + self.child1
                self.child2 = "0b" + self.child2
                self.append_generation(temporary_generation)
            else:
                self.dad = binary_population[i][2:].zfill(6)
                self.mom = binary_population[i + 1][2:].zfill(6)
                self.__init_child(crossing_points)
                self.mutate_person()
                self.dad = "0b" + self.dad
                self.mom = "0b" + self.mom
                self.child1 = "0b" + self.child1
                self.child2 = "0b" + self.child2
                self.append_generation(temporary_generation)
        for i in range(len(temporary_generation)):
            new_generation.append(int(temporary_generation[i], 2))
        return new_generation
