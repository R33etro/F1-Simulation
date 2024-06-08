
from ProjectInfo import ProjectInfo
from AuthorInfo import AuthorInfo
import tkinter as tk
from tkinter import messagebox
from Window import *
import pygame
from tkinter import simpledialog


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

        # muzyka ma grac w menu i podczas następnych okrążeń ma być ten drugi dźwięk
        #####MUSIC#####
        pygame.mixer.init()
        self.loading_screen_music = pygame.mixer.Sound("f1-music.mp3")
        self.new_lap_sound = pygame.mixer.Sound("cars-passing.mp3") # to jeszcze musze przyciąć zeby było krótsze

    def create_menu(self):
        
        """ 
        Function that creates the main menu of the simulation.
        """
        
        self.root.configure(bg= "#def0bb") #background color

        label_title = tk.Label(self.root, text="Main Menu", font=("Arial", 30, "bold"), bg="#def0bb")
        label_title.pack(pady=20) #20 px 


        #there will be start
        #button_start = tk.Button(self.root,activebackground="green", width=20, text="Start gry",cursor= "dotbox", relief="raised", font=("Arial", 16), bg="#baf051", fg="#000000", command=self.start_game)
        #button_start.pack(pady=10)

        button_rules = tk.Button(self.root, activebackground="green", width=20, text="Information about Project",cursor= "dotbox",relief="raised", font=("Arial", 16), bg="#92c926", fg="#000000", command=self.show_project_info)
        button_rules.pack(pady=10)

        button_author = tk.Button(self.root, activebackground="green", width=20, text="Information about authors",cursor= "dotbox",relief="raised", font=("Arial", 16), bg="#74a80f", fg="#000000", command=self.show_author_info)
        button_author.pack(pady=10)

        button_exit = tk.Button(self.root,activebackground="green", width=20, text="Exit", cursor= "dotbox",relief="raised",font=("Arial", 16), bg="#639109", fg="#000000", command=self.root.quit)
        button_exit.pack(pady=10)

    def start_game(self):
        pass

    
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
    
   