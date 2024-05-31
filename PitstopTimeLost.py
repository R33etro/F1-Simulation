import Randomizer
import RandomEvents
class TimeLostPitstop:
   
    def __init__(self, normalLost, rainLost, scLost):
        self.normalLost = normalLost
        self.rainLost = rainLost
        self.scLost = scLost

    def getTimeLost(self, isRain, isSC):
        if (isRain & isSC):
            return (self.rainLost/self.normalLost*self.scLost)+Randomizer.getRandomFactor(-1.0, 2.0)
        elif (isRain):
            return self.rainLost+Randomizer.getRandomFactor(-1.0, 2.0)
        elif (RandomEvents.isSC):
            return self.scLost+Randomizer.getRandomFactor(-1.0, 2.0)
        else:
            return self.normalLost+Randomizer.getRandomFactor(-1.0, 2.0)  
    