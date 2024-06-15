import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import Bolide
import Race
from tkinter import messagebox
import csv

class csvTechnologyDriversFormFile2:

    def __init__(self, root):

        self.root = root
        self.root.title("Race Configuration from csv File")

        self.entries = []
        self.track_var = tk.IntVar(value=1)
        self.laps_var = tk.IntVar(value=12)

        self.status_label = tk.Label(root, text="", padx=20, pady=10)
        self.status_label.grid(row=0, column=1, padx=10, pady=30)

        # Track selection
        track_label = tk.Label(root, text="Który tor:", font=("Arial", 10, "bold"))
        track_label.grid(row=1, column=0, padx=10, pady=10)
        tk.Radiobutton(root, text="SPA", variable=self.track_var, value=1).grid(row=1, column=1, padx=5, pady=5)
        tk.Radiobutton(root, text="RedBullRing", variable=self.track_var, value=2).grid(row=1, column=2, padx=5, pady=5)

        # Laps selection
        laps_label = tk.Label(root, text="Liczba okrążeń:", font=("Arial", 10, "bold"))
        laps_label.grid(row=2, column=0, padx=10, pady=10)
        laps_entry = tk.Entry(root, textvariable=self.laps_var)
        laps_entry.grid(row=2, column=1, padx=5, pady=5)

        # Submit button
        submit_button = tk.Button(root, text="Rozpocznij wyścig", command=self.submit)
        submit_button.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

        # dużo nowości i technologia csv
        file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                with open(file_path, 'r', newline='') as file:
                    csv_reader = csv.reader(file)

                    for row in csv_reader:
                        self.entries.append(row)

                    self.status_label.config(text=f"CSV file loaded: {file_path}")
            
            except Exception as e:
                self.status_label.config(text=f"Error: {str(e)}")

        
        

    def submit(self):

        """
        Function that reads the data from the entries from user and creates the cars.
        In case of incorrect data, the function displays an error message with Tk.messagebox.
        """

        try:
            cars = []
            for i in range(4):
                name = self.entries[i][0]
                speed = float(self.entries[i][1])
                skill = float(self.entries[i][2])
                strategy = float(self.entries[i][3])
                cars.append(Bolide.Bolide(name, speed, skill, strategy))

            numberOfLaps = self.laps_var.get()
            track = self.track_var.get()

            race = Race.Race(numberOfLaps, len(cars), track, cars)
            race.raceCalculations()
        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić prawidłowe wartości.")