import random

class Randomizer:

    """
    Class representing the Randomizer.
    Drawing random factors.
    """

    @staticmethod #nie potrzeba obiektu, żeby korzystać z metody
    def getRandomFactor(lower_bound, upper_bound, precision):
        random_number = random.uniform(lower_bound, upper_bound)
        return round(random_number, precision)
