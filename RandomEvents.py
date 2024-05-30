import Randomizer
class RandomEvents:
    # rainChance = 0.39
    # safetyCarChance = 0.56
    def __init__(self, rainChance, safetyCarChance):
        self.rainChance = rainChance
        self.safetyCarChance = safetyCarChance

    def isRain():
        probability = Randomizer.getRandomFactor(0.0, 1.0)
        if(probability < rainChance):
            return True
    def isSC():
        probability = Randomizer.getRandomFactor(0.0, 1.0)
        if(probability < safetyCarChance):
            return True