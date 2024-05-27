import random
#losuje liczbę typu float z zakresu
#metoda statyczna

class Randomizer:
    @staticmethod
    def getRandomFactor(lower_bound = -2.0, upper_bound = 2.0, precision = 2):
        random_number = random.uniform(lower_bound, upper_bound)
        return round(random_number, precision)

#print(Randomizer.getRandomFactor())