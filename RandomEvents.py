import Randomizer
class RandomEvents:
    # przykładowe wartości
    # rainChance = 0.39
    # safetyCarChance = 0.26
    def __init__(self, rainChance, safetyCarChance):
        self.rainChance = rainChance
        self.safetyCarChance = safetyCarChance

    def isRain(self, rainChance):
        probability = Randomizer.Randomizer.getRandomFactor(0.0, 1.0)
        # print({probability})
        if(probability < rainChance):
            return True
            # print('jest deszcz')
        # else:
        #     print("nie ma deszczu")

    def isSC(self, safetyCarChance):
        probability = Randomizer.Randomizer.getRandomFactor(0.0, 1.0)
        # print({probability})
        if(probability < safetyCarChance):
            return True
            # print("jest safety car")
        # else:
        #     print('niema sc')

# print(Randomizer.Randomizer.getRandomFactor(0.0, 1.0))
# testy - OK
# print(Randomizer.Randomizer.getRandomFactor(0.0, 1.0))
# Monza = RandomEvents(0.39, 0.26)
# Monza.isRain(Monza.rainChance)
# Monza.isSC(Monza.safetyCarChance)