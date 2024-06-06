import random
#losuje liczbę typu float z zakresu
#metoda statyczna

class Randomizer:
    @staticmethod
    def getRandomFactor(lower_bound, upper_bound, precision):
        random_number = random.uniform(lower_bound, upper_bound)
        return round(random_number, precision)

# print(Randomizer.getRandomFactor(-3.0, 3.0, 3))