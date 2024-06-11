import Randomizer

class RandomEvents:
    """
    Class representing random events during the simulation.
    They effect on the time of the lap.
    """

    def __init__(self, rainChance, safetyCarChance):

        """
        Constructor of the RandomEvents class.
        Initializes the chance of rain and safety car.

        Args:
            rainChance : float - chance of rain, value between 0 and 1
            safetyCarChance : float - chance of safety car, value between 0 and 1
        """
        self.rainChance = rainChance
        self.safetyCarChance = safetyCarChance

   
    def isRain(self):

        """
        Function that returns True if is rain, False otherwise.
        """

        probability = Randomizer.Randomizer.getRandomFactor(0.0, 1.0, 2)
        if(probability < self.rainChance ):   #tu self.rainChance bo to jest obiekt z tego RandomEvents, bez self jest nondefined
            return True
        else:
            return False

    def isSafetyCar(self, isRain):

        """
        Function that returns True if is safety car, False otherwise.
        Chance of safety car is higher when is rain.
        
        Args:
            isRain : bool - True if is rain, False otherwise
        """

        if isRain== True:
            probability = Randomizer.Randomizer.getRandomFactor(0.0, 0.7, 2)
        else:
            probability = Randomizer.Randomizer.getRandomFactor(0.0, 0.99, 2) 

        if(probability < self.safetyCarChance):
            return True
        else:
            return False