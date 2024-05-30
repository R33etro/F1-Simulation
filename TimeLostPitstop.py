import Randomizer
import RandomEvents
class TimeLostPitstop:
    # przykładowe współczynniki na strate czasu przy pitstopie
    # normalLost = 19.1
    # rainLost = 18.5
    # scLost = 14.2
    def __init__(self, normalLost, rainLost, scLost, rainChance, safetyCarChance):
        self.normalLost = normalLost
        self.rainLost = rainLost
        self.scLost = scLost

    def getTimeLost():
        if(RandomEvents.isRain & RandomEvents.isSC):
            return (rainLost/normalLost*scLost)+Randomizer.getRandomFactor(-1.0, 2.0)
        elif(RandomEvents.isRain):
            return rainLost+Randomizer.getRandomFactor(-1.0, 2.0)
        elif(RandomEvents.isSC):
            return scLost+Randomizer.getRandomFactor(-1.0, 2.0)
        else:
            return normalLost+Randomizer.getRandomFactor(-1.0, 2.0)  
    