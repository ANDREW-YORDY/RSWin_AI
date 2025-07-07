import tkinter as tk
from tkinter import *
from tkinter import ttk
from fileImg import Functions
from guiElements import GuiComponents
# from guiElements import fnGuiElements  --> antes de OOP.s


class RunScreenshot():

    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.geometry("900x650")
        self.root.title("SCREENSHOT")

        # Instancia de la calse Functions.
        self.fn = Functions()

        # Crear componentes GUI.
        self.gui = GuiComponents(self.fn)
        self.gui.fnGuiComponents(self.root)

        # Impementación anterior, sin OOP. Creación de la ventana principal.
        # root = Tk()
        # root.geometry("900x650")
        # root.title("SCREENSHOT")

        # frm = ttk.Frame(root, padding=10)
        # frm.grid()
        # frm.geometry("900x650")

    def run(self):
        """Ejecutar la Aplicación."""
        self.root.mainloop()


# Ejecutar solo si el archivo es principal.
if __name__ == "__main__":
    app = RunScreenshot()
    app.run()


# root.mainloop()
