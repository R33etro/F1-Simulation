import Bolide
import PitstopTimeLost
import RandomEvents

class Race:
    # NumberOfLaps = 15
    # Cars = [8]
    # track = 1

    def __init__(self, numberOfLaps, numberOfCars, track):
        self.numberOfLaps = numberOfLaps
        self.numberOfCars = numberOfCars   
        self.track = track  

    def getBolideStats():
        return

    def getPitstopTimeLost():
        return 

    def raceCalculations(self, track, numberOfLaps, numberOfCars):
        # czy nie lepiej obiekty random trzymać tutaj a nie global???
        if(track == 1): #SPA
            RandomEventsObject = RandomEvents.RandomEvents(0.64, 0.49)
            PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(19.1, 18.5, 14.2)
        else: #RedBullRing
            RandomEventsObject = RandomEvents.RandomEvents(0.35, 0.21)
            PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(17.7, 16.9, 15.3)

        # randomowe eventy występują i losują się na jedno okrążenie
        # deszcz odejmuje bolide.skill
        # safety car odejmuje bolide.strategy
        # jeśli nie ma random eventów to każdy jedzie zgodnie ze skillsami
        # jeśli są to odejmij staty i policz czas okrążenia
        # referencyjny czas jednego okrążenia i prawd. deszczu i SC 
        # dla np dwóch torów do wyboru z menu
        return

    def printTableEndOfRace():
        return                  

    def playBackgroundMusic():
        return

    def playRainSound():
        return        