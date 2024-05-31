import Bolide
import PitstopTimeLost
import RandomEvents

class Race:
    # NumberOfLaps = 15
    # Cars = [8]

    def __init__(self, numberOfLaps, numberOfCars, track):
        self.numberOfLaps = numberOfLaps
        self.numberOfCars = numberOfCars   
        self.track = track  
        # drawTrack

    # def drawTrack():
    #     # czy nie lepiej liste aut z czasem rzeczywistym - zdjęcie w sms
    #     return

    def setTrack(self, track):
        if(track == 1): #SPA
            RE = RandomEvents.RandomEvents(0.64, 0.49)
            PsTL = PitstopTimeLost.PitstopTimeLost(19.1, 18.5, 14.2, RE)
        else: #RedBullRing
            RE = RandomEvents.RandomEvents(0.35, 0.21)
            PsTL = PitstopTimeLost.PitstopTimeLost(17.7, 16.9, 15.3, RE)

    def getBolideStats():
        return

    def getPitstopTimeLost():
        return 

    def raceCalculations(self, PsTL, RE, numberOfLaps, numberOfCars):
        
        # randomowe eventy występują i losują się na jedno okrążenie
        # deszcz odejmuje bolide.skill
        # safety car odejmuje bolide.strategy
        # jeśli nie ma random eventów to każdy se jakoś jedzie
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