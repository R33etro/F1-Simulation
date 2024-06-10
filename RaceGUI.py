import tkinter as tk
from tkinter import ttk
from Race import Race


class RaceGUI:
    def __init__(self, root, race):
        self.root = root
        self.race = race
        Table = []
        index = 1
        for car in self.race.cars:
            Table.append([index, car.name, car.lap_time, car.gap])
            index += 1

        total_rows = len(Table)
        total_columns = len(Table[0])

        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = tk.Entry(self.root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, Table[i][j])


    def update_progress(self, currentLap):
        Table = []
        index = 1
        for car in self.race.cars:
            Table.append([index, car.name, car.lap_time, car.gap])
            index += 1

        total_rows = len(Table)
        total_columns = len(Table[0])

        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = tk.Entry(self.root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, Table[i][j])
        
