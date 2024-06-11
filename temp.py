# import tkinter as tk
# from tkinter import messagebox
# import Race
# import Bolide
# import RaceGUI

import tkinter as tk
from tkinter import messagebox

# Definiowanie klasy Kierowca
class Kierowca:
    def __init__(self, name="", value1=0, value2=0, value3=0):
        self.name = name
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def __repr__(self):
        return f"Kierowca(name={self.name}, value1={self.value1}, value2={self.value2}, value3={self.value3})"

# Funkcja wywoływana po kliknięciu przycisku
def submit():
    for i in range(8):
        drivers[i].name = entries[i][0].get()
        drivers[i].value1 = entries[i][1].get()
        drivers[i].value2 = entries[i][2].get()
        drivers[i].value3 = entries[i][3].get()
    
    selected_value = bottom_option.get()
    
    # Przykład: Wyświetlanie danych kierowców
    messagebox.showinfo("Informacja", f"Dane kierowców: {drivers}\nWybrana wartość: {selected_value}")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Formularz kierowców")

# Etykiety kolumn
columns = ["Imię", "Wartość 1", "Wartość 2", "Wartość 3"]
for idx, col in enumerate(columns):
    label = tk.Label(root, text=col, font=("Arial", 10, "bold"))
    label.grid(row=0, column=idx, padx=10, pady=5)

entries = []

# Tworzenie listy kierowców
drivers = [Kierowca() for _ in range(8)]

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

# Etykieta dla pola wyboru na dole
label_bottom_option = tk.Label(root, text="Która wartość:", font=("Arial", 10, "bold"))
label_bottom_option.grid(row=9, column=0, padx=10, pady=10)

# Tworzenie pola wyboru na dole
bottom_option = tk.StringVar(value="1")
bottom_option_menu = tk.OptionMenu(root, bottom_option, "1", "2")
bottom_option_menu.grid(row=9, column=1, padx=10, pady=10)

# Tworzenie i rozmieszczanie przycisku
submit_button = tk.Button(root, text="Wyślij", command=submit)
submit_button.grid(row=10, column=0, columnspan=4, padx=10, pady=10)

# Uruchomienie pętli głównej
root.mainloop()


#     race = Race.Race(10, 4, 1, drivers)
#     # gui = RaceGUI.RaceGUI(root, race)
#     Race.Race.raceCalculations()
    
# # Tworzenie głównego okna
# root = tk.Tk()
# root.title("Formularz kierowców")
