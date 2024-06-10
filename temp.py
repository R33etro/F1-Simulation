import tkinter as tk
from tkinter import messagebox
import Race
import Bolide
import RaceGUI

#kod do wrzucenia do menu

# Funkcja wywoływana po kliknięciu przycisku
def submit():
    for i in range(8):
        drivers[i].name = entries[i][0].get()
        drivers[i].value1 = entries[i][1].get()
        drivers[i].value2 = entries[i][2].get()
        drivers[i].value3 = entries[i][3].get()

    race = Race.Race(10, 4, 1, drivers)
    # gui = RaceGUI.RaceGUI(root, race)
    Race.Race.raceCalculations()
    
# Tworzenie głównego okna
root = tk.Tk()
root.title("Formularz kierowców")

class DriversForm:
    def __init__(self, parent):
        """
        Constructor of the DriversForm class.
        Args:
            parent : main window of the simulation"""
        
        self.parent = parent
        self.top = tk.Toplevel(parent) # okno nadrzędne
        self.columns = ["Name", "Speed", "Skill", "Strategy"]
        self.entries = []
        self.drivers = [Bolide.Bolide for _ in range(8)] # lista kierowców

        self.create_form()

    def create_form(self):
        """
        Function that creates the form for drivers' data input.
        """
        
        for idx, col in enumerate(self.columns):
            label = tk.Label(self.top, text=col, font=("Arial", 10, "bold"))
            label.grid(row=0, column=idx, padx=10, pady=5)

        for i in range(8):
            row_entries = []
            # Imię
            name_entry = tk.Entry(self.top)
            name_entry.grid(row=i+1, column=0, padx=5, pady=5)
            row_entries.append(name_entry)
            
            # Skill, Speed, Strategy
            for j in range(1, 4):
                value_entry = tk.Entry(self.top)
                value_entry.grid(row=i+1, column=j, padx=5, pady=5)
                row_entries.append(value_entry)
            
            self.entries.append(row_entries)

        # Tworzenie i rozmieszczanie przycisku
        submit_button = tk.Button(self.top, text="Sart race", command=submit)
        submit_button.grid(row=9, column=0, columnspan=5, padx=10, pady=10)
    
    def submit(self):
        for i in range(8):
            self.drivers[i] = Bolide.Bolide(
                name = self.entries[i][0].get(),
                speed = self.entries[i][1].get(),
                skill = self.entries[i][2].get(),
                strategy = self.entries[i][3].get()
            )

        race = Race.Race(10, 4, 1, self.drivers)
        race.raceCalculations
        self.top.destroy()

