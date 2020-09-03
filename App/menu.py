from .Entities.Crossing.mask_cross import MaskCross
from .Entities.Crossing.one_point_cross import OnePointCross
from .Entities.Crossing.two_point_cross import TwoPointCross
from .Modules.extremum_values import ExtremumValues
from .Entities.Population.blanket import Blanket
from .Entities.Population.selective import Selective
from .Entities.Population.shotgun import Shotgun
from .Entities.Selection.roulette import Roulette
from .Entities.Selection.tournament import Tournament


class Menu:
    def __init__(self):
        self.extremum = 0
        self.population = 0
        self.selection = 0
        self.crossing = 0

    def __choose_extremum(self):
        while True:
            print("Select one of the values: ")
            print("Input:\n\t 0 - You search MINIMUM value\n\t 1 - You search MAXIMUM value")
            inp = int(input())
            if inp == 0:
                self.extremum = 0
                print("You search min value\n")
                break
            elif inp == 1:
                self.extremum = 0
                print("You search max value\n")
                break
            else:
                print("Wrong argument\n")

    def __choose_population(self):
        while True:
            print("Select one of the values: ")
            print("Input:\n\t 0 - For BLANKET\n\t 1 - For SELECTIVE\n\t 2 - For SHOTGUN")
            inp = int(input())
            if inp == 0:
                self.population = inp
                print("You select BLANKET population\n")
                break
            elif inp == 1:
                self.population = inp
                print("You select SELECTIVE population\n")
                break
            elif inp == 2:
                self.population = inp
                print("You select SHOTGUN population\n")
                break
            else:
                print("Wrong argument\n")

    def __choose_selection(self):
        while True:
            print("Select one of the values: ")
            print("Input:\n\t 0 - For TOURNAMENT\n\t 1 - For ROULETTE")
            inp = int(input())
            if inp == 0:
                self.selection = inp
                print("You select TOURNAMENT selection\n")
                break
            elif inp == 1:
                self.selection = inp
                print("You select ROULETTE selection\n")
                break
            else:
                print("Wrong argument\n")

    def __choose_crossing(self):
        while True:
            print("Select one of the values: ")
            print("Input:\n\t 0 - For ONE_POINT_CROSS\n\t 1 - For TWO_POINT_CROSS\n\t 2 - For MASK_CROSS")
            inp = int(input())
            if inp == 0:
                self.crossing = inp
                print("You select ONE_POINT_CROSS crossing\n")
                break
            elif inp == 1:
                self.crossing = inp
                print("You select TWO_POINT_CROSS crossing\n")
                break
            elif inp == 2:
                self.crossing = inp
                print("You select MASK_CROSS crossing\n")
                break
            else:
                print("Wrong argument\n")

    def main(self):
        extremum_value = ExtremumValues()
        self.__choose_extremum()
        self.__choose_population()
        if self.population == 0:
            generation = Blanket().generation
            print("Initial population: ", generation)
            result = extremum_value.value(generation, self.extremum)
            print("The MINIMUM value of function = " + str(result))
            return None
        self.__choose_selection()
        self.__choose_crossing()

        generation = Selective().generation
        print("Initial population: ", generation)
        result = extremum_value.value(generation, self.extremum)
        print("The MINIMUM value of function = " + str(result))

        for i in range(10):
            new_generation = MaskCross(Tournament(self.extremum, generation).selection).new_generation
            print(new_generation)

            generation = new_generation
            result = extremum_value.value(generation, self.extremum)
            print("The MINIMUM value of function = ", result, "\n")
