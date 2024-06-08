import Randomizer

class RandomEvents:
    def __init__(self, rainChance, safetyCarChance):
        self.rainChance = rainChance
        self.safetyCarChance = safetyCarChance

    def isRain(self):
        """self bo jest tworzony obiekt w klasie Race i self jest odwołaniem do obiektu klasy RandomEvents. """
        probability = Randomizer.Randomizer.getRandomFactor(0.0, 1.0, 2)
        if(probability < self.rainChance ):   #tu self.rainChance bo to jest obiekt z tego RandomEvents, bez self jest nondefined
            return True
        else:
            return False

    def isSafetyCar(self, isRain):
        if isRain== True:
            probability = Randomizer.Randomizer.getRandomFactor(0.0, 0.7, 2)
        else:
            probability = Randomizer.Randomizer.getRandomFactor(0.0, 1.0, 2) #szansa na safetycar jest większa podczas deszczu

        if(probability < self.safetyCarChance):
            return True
        else:
            return False