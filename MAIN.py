import tkinter as tk
from Menu import Menu


if __name__ == "__main__":
    """
    Function main that runs the simulation. Creates the main men window of the simulation.
    """
    root = tk.Tk()
    root.title("Formula 1 Simulation")
    menu = Menu(root)
    root.mainloop()