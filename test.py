from App.Entities.Population.blanket import Blanket
from App.Entities.Population.selective import Selective
from App.Entities.Population.shotgun import Shotgun
from App.Entities.Selection.roulette import Roulette
from App.Entities.Selection.tournament import Tournament


def test():
    print("You search min value\n")
    gen = Selective().generations
    print(gen)
    print(Tournament(True, gen).selection)
test()
