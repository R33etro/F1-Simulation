import Randomizer
class RandomEvents:
    # rainChance = 0.39
    # safetyCarChance = 0.56
    def __init__(self, rainChance, safetyCarChance):
        self.rainChance = rainChance
        self.safetyCarChance = safetyCarChance

    def isRain():
        probability = Randomizer.getRandomFactor(0.0, 1.0)
        print({probability})
        if(probability < rainChance):
            print('1')
            return True
    def isSC():
        probability = Randomizer.getRandomFactor(0.0, 1.0)
        print(probability)
        if(probability < safetyCarChance):
            print("1")
            return True