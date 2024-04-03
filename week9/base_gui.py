from tkinter import *
from abc import ABC, abstractmethod

class BaseGUI(ABC):
    def __init__(self, title, dimensions):
        self.window = self.create_window(title, dimensions)
        self.create_widgets()
    
    def create_window(self, title, dimensions):
        window = Tk()
        window.title(title)
        window.geometry(dimensions)
        return window
    
    @abstractmethod
    def create_widgets(self):
        pass
    
    def run(self):
        self.window.mainloop()