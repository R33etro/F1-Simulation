import Randomizer

class PitstopTimeLost:
    """
    Class representing the time lost during a pitstop.
    """

    def __init__(self, normalLost, rainLost, scLost):

        """
        Constructor of the PitstopTimeLost class.
        Initializes the time lost during a pitstop.
        Args:
            normalLost : float - time lost during a normal pitstop
            rainLost : float - time lost during a pitstop in case of rain
            scLost : float - time lost during a pitstop in case of safety car
        """

        self.normalLost = normalLost
        self.rainLost = rainLost
        self.scLost = scLost

    def getPitstopTimeLost(self, isRain, isSafetyCar):

        """
        Function that returns the time lost during a pitstop.
        
        Args:
            isRain : bool - True if is rain, False otherwise
            isSafetyCar : bool - True if is safety car, False otherwise
        """

        if (isRain & isSafetyCar):
            return (self.rainLost/self.normalLost*self.scLost)+Randomizer.Randomizer.getRandomFactor(0.0, 4.0, 2)
        elif (isRain):
            return self.rainLost+Randomizer.Randomizer.getRandomFactor(0.0, 3.5, 2)
        elif (isSafetyCar):
            return self.scLost+Randomizer.Randomizer.getRandomFactor(0.0, 2.5, 2)
        else:
            return self.normalLost+Randomizer.Randomizer.getRandomFactor(0.0, 2.0, 2)  
    