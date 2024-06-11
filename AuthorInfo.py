import tkinter as tk


class AuthorInfo:

    """ Class representing information about the authors of the game. """

    def __init__(self):
        
        """ Constructor of the AuthorInfo class. """
        
        self.window = tk.Toplevel()
        self.window.title("Infomacje o autorze")
        self.text = tk.Text(self.window, width=40, height=10)
        self.text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.author_info = """  \n
                                Patrycja Bernard numer indeksu 276026\n
                                Piotr Kulej numer indeksu 281085 - lider zespołu\n"""
        
        
    def get_author_info(self):
        
        """ Function that displays information about the author."""

        self.text.configure(font=("Arial", 12), spacing1=8)
        self.text.insert(tk.END, self.author_info)
        self.text.configure(state=tk.DISABLED)