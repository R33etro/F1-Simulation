import Randomizer
import RandomEvents
class PitstopTimeLost:
   
    def __init__(self, normalLost, rainLost, scLost):
        self.normalLost = normalLost
        self.rainLost = rainLost
        self.scLost = scLost

    def getPitstopTimeLost(self, isRain, isSafetyCar):
        if (isRain & isSafetyCar):
            return (self.rainLost/self.normalLost*self.scLost)+Randomizer.Randomizer.getRandomFactor(0.0, 4.0, 2)
        elif (isRain):
            return self.rainLost+Randomizer.Randomizer.getRandomFactor(0.0, 3.0, 2)
        elif (isSafetyCar):
            return self.scLost+Randomizer.Randomizer.getRandomFactor(0.0, 3.0, 2)
        else:
            return self.normalLost+Randomizer.Randomizer.getRandomFactor(0.0, 2.0, 2)  
    