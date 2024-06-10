import tkinter as tk

class ProjectInfo:

    """
    Class representing the information about the project.
    """

    def __init__(self):

        """
        Constructor of the ProjectInfo class.
        """
        self.window = tk.Toplevel()
        self.window.title("Informations about the project")
        self.text = tk.Text(self.window, width=40, height=10)
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.project_info = """Symulacja przewiduje 8 samochodów oraz kilka okrążeń. 
                            Każdy samochód-kierowca ma pewny współczynnik szansy na wygraną zależną od 
                            np. umiejętności kierowcy, szybkości auta, strategii zespołu. 
                            W trakcie symulacji będą elementy losowe np. deszcz, wyjazd samochodu bezpieczeństwa, 
                            o odpowiednim prawdopodobieństwie wystąpienia, 
                            które będą wpływały na kolejność aut po każdym okrążeniu 
                            oraz straty czasowe podczas pitstopów. Liczba elementów losowych 
                            oraz innych współczynników może ulec zmianie. Projekt przewiduje interfejs graficzny."""
  
    def get_project_info(self):
        
        self.text.configure(font=("Arial", 12), spacing1=8)
        self.text.insert(tk.END, self.project_info)
        self.text.configure(state=tk.DISABLED)