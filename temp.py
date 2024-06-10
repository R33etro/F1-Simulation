import tkinter as tk
from tkinter import messagebox
import Race
import Bolide
import RaceGUI

# Funkcja wywoływana po kliknięciu przycisku
def submit():
    for i in range(8):
        drivers[i].name = entries[i][0].get()
        drivers[i].value1 = entries[i][1].get()
        drivers[i].value2 = entries[i][2].get()
        drivers[i].value3 = entries[i][3].get()

    Race.Race(10, 4, 1, drivers)
    Race.Race.raceCalculations(RaceGUI.RaceGUI(root, race))
    
# Tworzenie głównego okna
root = tk.Tk()
root.title("Formularz kierowców")

# Etykiety kolumn
columns = ["Imię", "Speed", "Skill", "Strategy"]
for idx, col in enumerate(columns):
    label = tk.Label(root, text=col, font=("Arial", 10, "bold"))
    label.grid(row=0, column=idx, padx=10, pady=5)

entries = []

# Tworzenie listy kierowców
drivers = [Bolide.Bolide for _ in range(8)]

for i in range(8):
    row_entries = []
    # Imię
    name_entry = tk.Entry(root)
    name_entry.grid(row=i+1, column=0, padx=5, pady=5)
    row_entries.append(name_entry)
    
    # Trzy wartości liczbowe
    for j in range(1, 4):
        value_entry = tk.Entry(root)
        value_entry.grid(row=i+1, column=j, padx=5, pady=5)
        row_entries.append(value_entry)
    
    entries.append(row_entries)

# Tworzenie i rozmieszczanie przycisku
submit_button = tk.Button(root, text="Wyślij", command=submit)
submit_button.grid(row=9, column=0, columnspan=5, padx=10, pady=10)

# Uruchomienie pętli głównej
root.mainloop()