import PitstopTimeLost
import RandomEvents
import Randomizer
import tkinter as tk
import time
from pygame import mixer
import csv
from tkinter import filedialog


class Race:

    """
    The Race class simulates a racing event based on provided parameters such as number of laps, number of cars, track type, and car details.

    Args:
    numberOfLaps: int, specifies the total number of laps for the race.
    numberOfCars: int, represents the number of cars participating in the race.
    track: int, indicates the type of track (1 for SPA, 2 for RedBullRing).
    cars: List of Bolide objects, each representing a car with specific attributes (name, speed, skill, strategy)."""
    
    def __init__(self, numberOfLaps, numberOfCars, track, cars):
        """"
        Constructor od Race class. Initializes race parameters."""
        self.numberOfLaps = numberOfLaps
        self.numberOfCars = numberOfCars
        self.track = track
        self.cars = cars

    def raceCalculations(self):
        """
        Function that simulate the racing calculations for each lap of the race."""

        laaap = 0

        if self.track == 1:  # SPA
                referenceTime = 106.168  # 106 sekund czyli minuta 46
                RandomEventsObject = RandomEvents.RandomEvents(0.64, 0.49)
                PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(19.1, 18.5, 14.2)
        else:  # track == 2 #RedBullRing
                referenceTime = 64.391  # 64 sekundy czyli minuta 04
                RandomEventsObject = RandomEvents.RandomEvents(0.35, 0.21)
                PitstopTimeLostObject = PitstopTimeLost.PitstopTimeLost(17.7, 16.9, 15.3)

        
        for currentLap in range(0, self.numberOfLaps):

            isRain = RandomEventsObject.isRain()
            isSafetyCar = RandomEventsObject.isSafetyCar(isRain)

            for car in range(0, self.numberOfCars):
                if currentLap == 0:
                    self.cars[car].gap += 0.1 * car

                if currentLap == int(self.numberOfLaps / 3) or currentLap == int(self.numberOfLaps * 2 / 3):
                    self.cars[car].lap_time += PitstopTimeLostObject.getPitstopTimeLost(isRain, isSafetyCar)

                if currentLap == int(self.numberOfLaps * 4 / 5):
                    if Randomizer.Randomizer.getRandomFactor(0.0, 1.0, 2) > self.cars[car].strategy:
                        self.cars[car].lap_time += PitstopTimeLostObject.getPitstopTimeLost(isRain, isSafetyCar)

                if isSafetyCar:
                    self.cars[car].lap_time += 12.0

                if isRain:
                    upper_bound = 3.0 - (self.cars[car].speed + self.cars[car].skill + (self.cars[car].strategy - 0.15))
                    random_race_lost = Randomizer.Randomizer.getRandomFactor(0.0, upper_bound, 3)
                else:
                    upper_bound = 3.0 - (self.cars[car].speed + self.cars[car].skill + self.cars[car].strategy)
                    random_race_lost = Randomizer.Randomizer.getRandomFactor(0.0, upper_bound, 3)

                #lap time = reference time + random time lost + (if happend) pitstop time lost + safety car lost
                self.cars[car].lap_time += (referenceTime + random_race_lost)

            self.cars.sort(key=lambda x:( x.lap_time + x.gap))
            for i in range(1, self.numberOfCars):
                self.cars[i].gap += (self.cars[i].lap_time - self.cars[i-1].lap_time)
            self.cars[0].gap = 0

            laaap += 1

            for car in self.cars:
                car.lap_time = 0

        self.show_table(laaap)

    def show_table(self, Lap):
        
        """
        Function to show the table with the results of the simulation.
        """

        root = tk.Tk()
        root.title(f"Race Results on lap: {Lap}")

        ###MUSIC###
        mixer.init()
        mixer.music.load("engine-noise.mp3")
        mixer.music.play()

        table = []
        for car in self.cars:
            table.append([car.name, round(car.gap, 3)])

        total_rows = len(table)
        total_columns = len(table[0])

        for i in range(total_rows):
            for j in range(total_columns):
                e = tk.Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold'))
                e.grid(row=i, column=j)
                e.insert(tk.END, table[i][j])

        # csv technology
        write_button = tk.Button(root, width=20, text="Write results to csv file", cursor="dotbox", relief="raised", font=("Arial", 16), bg="#baf051", fg="#000000", command=self.write_csv_file(table))
        write_button.grid(row=6, column=0, padx=10, pady=10)

    def write_csv_file(self, table):
        """
        Function to write the results of the simulation to a csv file.
        Args:
            table : list - list of lists with the results of the simulation."""
      
        with open("results.csv", 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for row in table:
                csv_writer.writerow(row)
