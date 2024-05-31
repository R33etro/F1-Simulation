import random
#losuje liczbę typu float z zakresu
#metoda statyczna

class Randomizer:
    @staticmethod
    def getRandomFactor(lower_bound, upper_bound):
        random_number = random.uniform(lower_bound, upper_bound)
        return round(random_number, 2)

# print(Randomizer.getRandomFactor(0.0, 1.0))