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
            # referencyjny czas = 1.23.456
            RandomEventsObject = RandomEvents.RandomEvents(0.64, 0.49)
            PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(19.1, 18.5, 14.2)
        else: #RedBullRing
            # referencyjny czas = 1.01.202
            RandomEventsObject = RandomEvents.RandomEvents(0.35, 0.21)
            PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(17.7, 16.9, 15.3)

        # pętla for na tyle ile okrążeń
        # 
        # statrują z pól startowych a nie "z jednej linii" więc każdy ma na starcie troche 0,5 sekundy straty do kolejnego
        # 
        # na początku losuje random eventy które występują tylko na jedno okrążenie
        # deszcz odejmuje bolide.skill po równo
        # safety car odejmuje bolide.speed po równo
        # 
        # pitstopy: każdy musi zrobić dwa przez cały wyścig i jeden losuje z random na podstawie bolid.strategy(im większe strategy tym mniejsza szansa)
        # np ilosc okrążeń /3 i wszyscy robią na tym samym okrążeniu po dwa
        #
        # wylosuj +/- ile (-3.000 - +3.000) sekund przypadkowych dla każdego kierowcy dla jednego okrążenia
        # 
        # policz czas okrążenia - tylko jak??
        # referencyjny czas + pitstop +/- przypadek
        # reszta statów do innych rzeczy
        # 
        # wyprzedzanie: jeśli kierowca jest mniej niż sekunde za poprzednim to:
        # dodaj bolid.speed i bolid.skill z random czynnikiem(0,01 - 0,10) różnym dla obu, porównaj i jeśli ten z tyłu ma większy wynik - zamien pozycje
        # zakaz wyprzedzania przy safety car
        # 
        # wypisz kolejność aut z czasami okrążeń
        #
        # 
        # referencyjne prawd. deszczu i SC 
        # dla np dwóch torów do wyboru z menu
        return

    def printTableEndOfRace():
        return                  

    def playBackgroundMusic():
        return

    def playRainSound():
        return        