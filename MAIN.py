import tkinter as tk
from tkinter import ttk
import Race
import RaceGUI
import Menu

if __name__ == "__main__":
    root = tk.Tk()
    race = Race.Race(10, 4, 2)
    gui = RaceGUI.RaceGUI(root, race)
    menuu = Menu.Menu(root)
    race.raceCalculations(gui)
    root.mainloop()



