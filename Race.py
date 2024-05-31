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

    def setTrack():
        if(track == 1):
            ptl = PitstopTimeLost(19.1, 18.5, 14.2)
            re = RandomEvents(0.39, 0.56)
        else:
            ptl = PitstopTimeLost(18.7, 17.9, 15.3)
            re = RandomEvents(0.45, 0.61)

    def getBolideStats():
        return

    def getPitstopTimeLost():
        return 

    def raceCalculations():
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