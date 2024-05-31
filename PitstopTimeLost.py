import Randomizer
import RandomEvents
class PitstopTimeLost:
    # przykładowe współczynniki na strate czasu przy pitstopie
    # normalLost = 19.1
    # rainLost = 18.5
    # scLost = 14.2
    # przykładowe wartości random events
    # rainChance = 0.39
    # safetyCarChance = 0.26
    def __init__(self, normalLost, rainLost, scLost, RE):
        self.normalLost = normalLost
        self.rainLost = rainLost
        self.scLost = scLost

    def getTimeLost(self, normalLost, rainLost, scLost):
        if(RandomEvents.isRain & RandomEvents.isSC):
            return (rainLost/normalLost*scLost)+Randomizer.Randomizer.getRandomFactor(-1.0, 2.0)
        elif(RandomEvents.isRain):
            return rainLost+Randomizer.getRandomFactor(-1.0, 2.0)
        elif(RandomEvents.isSC):
            return scLost+Randomizer.getRandomFactor(-1.0, 2.0)
        else:
            return normalLost+Randomizer.getRandomFactor(-1.0, 2.0)  
