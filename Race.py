import Bolide
import PitstopTimeLost
import RandomEvents
import Randomizer

class Race:
    # NumberOfLaps = 15
    # Lista Cars = [8] # tutaj też kolejność najpierw na starcie potem po każdym okrążeniu 
    # track = 1


    def __init__(self, numberOfLaps, numberOfCars, track):
        self.numberOfLaps = numberOfLaps
        self.numberOfCars = numberOfCars
        self.track = track
        self.cars = [Bolide.Bolide('Ver', 0.90, 0.90, 0.90),
                     Bolide.Bolide('Nor', 0.90, 0.90, 0.90),
                     Bolide.Bolide('Sai', 0.90, 0.90, 0.90),
                     Bolide.Bolide('Kub', 0.90, 0.90, 0.90)]

    def raceCalculations(self):
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
            print('\n-----------------------------------------------------------------')
            print('lap:', currentLap+1, 'is rain:', isRain, 'is sc:', isSafetyCar, '\n')

            for car in range (0, self.numberOfCars):

                if(currentLap == 0):
                    #każdemu kierowcy przypisz na start +0.1 od poprzednika z racji różnicy odległości pól startowych
                    self.cars[car].lap_time += 0.1*car
                    # print('roznica na starcie ',self.cars[car].name,' ', self.cars[car].lap_time,'\n')


                if(currentLap == int(self.numberOfLaps/3) or currentLap == int(self.numberOfLaps*2/3)):
                    #każdemu kierowcy przypisz pitstop_time_lost do bolide.lap_time
                    self.cars[car].lap_time += PitstopTimeLostObject.getPitstopTimeLost(isRain, isSafetyCar)
                    print('pitstop\n')

                if(currentLap == int(self.numberOfLaps*4/5)):
                    if(Randomizer.Randomizer.getRandomFactor(0.0, 1.0, 2) > self.cars[car].strategy):
                        #jeśli wylosował - kierowcy przypisz do bolide.lap_time
                        print('dodatkowy pitstop', self.cars[car].name ,'\n')
                        self.cars[car].lap_time += PitstopTimeLostObject.getPitstopTimeLost(isRain, isSafetyCar)

                if(isSafetyCar): # safety car dodaje do bolide.laptime +12 sekund 
                    self.cars[car].lap_time += 12
                    # print('czy jest dodał 12 sekund z okazji safety car')


                if(isRain): # deszcz odejmuje od bolide.skill -0.15 
                    upper_bound = 3.0 - (self.cars[car].speed + self.cars[car].skill + (self.cars[car].strategy - 0.15))
                    random_race_lost = Randomizer.Randomizer.getRandomFactor(0.0, upper_bound, 3)
                else:
                    upper_bound = 3.0 - (self.cars[car].speed + self.cars[car].skill + self.cars[car].strategy)
                    random_race_lost = Randomizer.Randomizer.getRandomFactor(0.0, upper_bound, 3)
                    # print(random_race_lost,'\n')

                #random_race_lost dodaje czas od 0.000 do 3.000-statystyki im lepsze statystyki tym mniej dodaje 
                # car.lap_time = reference_time + random_race_factor + safety car(jeśli jest) + pitstop(jeśli jest)
                self.cars[car].lap_time += (referenceTime + random_race_lost)

                # koniec pętli przypisującej lap_time
                # self.cars.sort(key=lambda x:x.lap_time)
                # print(self.cars[car].name,' ', round(self.cars[car].lap_time, 3)-referenceTime*currentLap)
                
        
            # wpisz listę kierowców od najlepszego czasu - koniec
            self.cars.sort(key=lambda x:x.lap_time)
            for car in range (0, self.numberOfCars):
                print(self.cars[car].name,' ', round(self.cars[car].lap_time, 3))
                self.cars[car].lap_time = 0
            


    def printTableEndOfRace(): #lista aut jest w klasie więc tutaj możemy robić jakąś ładną tabelke
        return                  

    def playBackgroundMusic():
        return

    def playRainSound():
        return        

race = Race(10,4,2)
race.raceCalculations()