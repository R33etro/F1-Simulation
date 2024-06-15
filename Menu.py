from ProjectInfo import ProjectInfo
from AuthorInfo import AuthorInfo
import tkinter as tk
from pygame import mixer
import DriversForm
import csvTechnologyDriversFormFile2

class Menu:
    """
    Class representing the main menu of the simulation.
    """
    
    def __init__(self, root):
        """
        Constructor of the Menu class. 

        Attributes:
            root : main window of the simulation
        """
        self.root = root 
        self.create_menu()

        #####MUSIC#####
        mixer.init()
        mixer.music.load("f1-music.mp3")
        mixer.music.play()
        
         

    def create_menu(self):

        """ 
        Function that creates the main menu of the simulation.
        Creates buttons that allow the user to choose between the drivers' form, information about the project, 
        information about the authors start and exit the simulation.

        """
        self.root.configure(bg="#def0bb") #background color

        label_title = tk.Label(self.root, text="Main Menu", font=("Arial", 30, "bold"), bg="#def0bb")
        label_title.grid(row=0, column=0, columnspan=2, pady=20)

        #buttons

        button_start = tk.Button(self.root, activebackground="green", width=20, text="Drivers Form", cursor="dotbox", relief="raised", font=("Arial", 16), bg="#baf051", fg="#000000", command=self.show_drivers_form)
        button_start.grid(row=1, column=0, padx=10, pady=10)

        button_csv = tk.Button(self.root, activebackground="green", width=20, text="Open csv file", cursor="dotbox", relief="raised", font=("Arial", 16), bg="#baf051", fg="#000000", command=self.load_csv_file)
        button_csv.grid(row=2, column=0, padx=10, pady=10)

        button_rules = tk.Button(self.root, activebackground="green", width=20, text="Information about Project", cursor="dotbox", relief="raised", font=("Arial", 16), bg="#92c926", fg="#000000", command=self.show_project_info)
        button_rules.grid(row=3, column=0, padx=10, pady=10)

        button_author = tk.Button(self.root, activebackground="green", width=20, text="Information about authors", cursor="dotbox", relief="raised", font=("Arial", 16), bg="#74a80f", fg="#000000", command=self.show_author_info)
        button_author.grid(row=4, column=0, padx=10, pady=10)

        button_exit = tk.Button(self.root, activebackground="green", width=20, text="Exit", cursor="dotbox", relief="raised", font=("Arial", 16), bg="#639109", fg="#000000", command=self.root.quit)
        button_exit.grid(row=5, column=0, padx=10, pady=10)

    def show_drivers_form(self):

        """
        Function displaying the form for entering the drivers' data.
        """

        form_window = tk.Toplevel(self.root)
        drivers_form = DriversForm.DriversForm(form_window) 

    def load_csv_file(self):

        filled_form_window = tk.Toplevel(self.root)
        csv_technology_file2 = csvTechnologyDriversFormFile2.csvTechnologyDriversFormFile2(filled_form_window)  

    def show_project_info(self):

        """
        Function displaying information about the project.
        """

        project = ProjectInfo()
        project.get_project_info()

    def show_author_info(self):

        """
        Function displaying information about the authors.
        """
        
        authors = AuthorInfo()
        authors.get_author_info()
