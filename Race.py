import Bolide
import PitstopTimeLost
import RandomEvents

class Race:
    # NumberOfLaps = 15
    # Lista Cars = [8] # tutaj też kolejność najpierw na starcie potem po każdym okrążeniu 
    # track = 1


    def __init__(self, numberOfLaps, numberOfCars, track):
        self.numberOfLaps = numberOfLaps
        self.numberOfCars = numberOfCars   
        self.track = track  

    # def getBolideStats():
    #     return

    # def getPitstopTimeLost():
    #     return 

    def raceCalculations(self, track, numberOfLaps, numberOfCars):
        # czy nie lepiej obiekty random trzymać tutaj a nie global???
        self.track = track
        self.numberOfLaps = numberOfLaps
        self.numberOfCars = numberOfCars

        if(self.track == 1): #SPA
            referenceTime = 83.456 #83 sekund czyli minuta 23
            RandomEventsObject = RandomEvents.RandomEvents(0.64, 0.49)
            PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(19.1, 18.5, 14.2)
        else: # track == 2 #RedBullRing
            referenceTime = 61.202 #61 sekund czyli minuta 01
            RandomEventsObject = RandomEvents.RandomEvents(0.35, 0.21)
            PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(17.7, 16.9, 15.3)

        for currentLap in range (0, self.numberOfLaps):

            isRain = RandomEventsObject.isRain()
            isSafetyCar = RandomEventsObject.isSafetyCar(isRain)

            for car in range (0, numberOfCars):
                #każdemu kierowcy przypisz +0.1 sekundy z racji dalszego miejsca od linii startu
                if(currentLap == 0):
                    car.lap_time += 0.1
                if(currentLap == numberOfLaps/3 | currentLap == numberOfLaps*2/3):
                    #każdemu kierowcy przypisz do bolide.lap_time
                    PitstopTimeLostObject.getPitstopTimeLost(isRain, isSafetyCar)
                if(currentLap == numberOfLaps*3/4):
                    #każdemu kierowcy przypisz do bolide.lap_time
                    if(Randomizer.getRandomFactor(0.0, 1.0) > car.strategy):
                        PitstopTimeLostObject.getPitstopTimeLost(isRain, isSafetyCar)

                if(isSafetyCar): # safety car dodaje do bolide.laptime +12 sekund 
                    car.lap_time += 12

                if(isRain): # deszcz odejmuje od bolide.skill -0.15 
                    random_race_lost = Randomizer.getRandomFactor(0.000, (3.000 - (car.speed + car.skill + (car.strategy - 0.15))), 3)
                else:
                    random_race_lost = Randomizer.getRandomFactor(0.000, (3.000 - (car.speed + car.skill + car.strategy)), 3)

                #random_race_lost dodaje czas od 0.000 do 3.000-statystyki im lepsze statystyki tym mniej dodaje 
                # car.lap_time = reference_time + random_race_factor + safety car(jeśli jest) + pitstop(jeśli jest)
                car.lap_time += referenceTime + random_race_lost

                # koniec pętli przypisującej lap_time
        
            # wpisz listę kierowców od najlepszego czasu - koniec
       

    def printTableEndOfRace():
        return                  

    def playBackgroundMusic():
        return

    def playRainSound():
        return        