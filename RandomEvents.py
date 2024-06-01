import Randomizer

class RandomEvents:
    def __init__(self, rainChance, safetyCarChance):
        self.rainChance = rainChance
        self.safetyCarChance = safetyCarChance

    def isRain(self):
        """self bo klasa zapamiętuje w inicie rainChance z Maina(FORMULA) i self jest odwołaniem do obiektu klasy RandomEvents. """
        probability = Randomizer.Randomizer.getRandomFactor(0.0, 1.0)
        if(probability < self.rainChance ):   #tu self.rainChance bo to jest obiekt z tego RandomEvents, bez self jest nondefined
            return True
        else:
            return False
    def isSC(self, isRain):
        
        if isRain== True:
            probability = Randomizer.Randomizer.getRandomFactor(0.0, 0.7)
        else:
            probability = Randomizer.Randomizer.getRandomFactor(0.0, 1.0)

        if(probability < self.safetyCarChance):
            return True
        else:
            return False