import tkinter as tk
import Bolide
import Race
from tkinter import messagebox

class DriversForm:

    def __init__(self, root):
        self.root = root
        self.root.title("Race Configuration")

        self.entries = []
        self.track_var = tk.IntVar(value=1)
        self.laps_var = tk.IntVar(value=10)

        # Etykiety kolumn
        columns = ["Name", "Speed", "Skill", "Strategy"]
        for idx, col in enumerate(columns):
            label = tk.Label(root, text=col, font=("Arial", 10, "bold"))
            label.grid(row=0, column=idx, padx=10, pady=5)

        for i in range(2):
            row_entries = []
            for j in range(4):
                entry = tk.Entry(root)
                # entry.insert(0,"0.9")
                entry.grid(row=i+1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Track selection
        track_label = tk.Label(root, text="Która wartość:", font=("Arial", 10, "bold"))
        track_label.grid(row=9, column=0, padx=10, pady=10)
        tk.Radiobutton(root, text="SPA", variable=self.track_var, value=1).grid(row=9, column=1, padx=5, pady=5)
        tk.Radiobutton(root, text="RedBullRing", variable=self.track_var, value=2).grid(row=9, column=2, padx=5, pady=5)

        # Laps selection
        laps_label = tk.Label(root, text="Liczba okrążeń:", font=("Arial", 10, "bold"))
        laps_label.grid(row=10, column=0, padx=10, pady=10)
        laps_entry = tk.Entry(root, textvariable=self.laps_var)
        laps_entry.grid(row=10, column=1, padx=5, pady=5)

        # Submit button
        submit_button = tk.Button(root, text="Wyślij", command=self.submit)
        submit_button.grid(row=11, column=0, columnspan=4, padx=10, pady=10)
        

    def submit(self):
        try:
            cars = []
            for i in range(2):
                name = self.entries[i][0].get()
                speed = float(self.entries[i][1].get())
                skill = float(self.entries[i][2].get())
                strategy = float(self.entries[i][3].get())
                cars.append(Bolide.Bolide(name, speed, skill, strategy))

            numberOfLaps = int(self.laps_var.get())
            track = int(self.track_var.get())

            race = Race.Race(numberOfLaps, len(cars), track, cars)
            race.raceCalculations()
        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić prawidłowe wartości.")