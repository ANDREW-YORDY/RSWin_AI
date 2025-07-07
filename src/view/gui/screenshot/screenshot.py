import tkinter as tk
from tkinter import *
from tkinter import ttk
from fileImg import test_pil
from guiElements import fnGuiElements




# Creación de la ventana principal.
root = Tk()
root.geometry("900x650")
root.title("SCREENSHOT")

fnGuiElements(root)


# frm = ttk.Frame(root, padding=10)
# frm.grid()
# frm.geometry("900x650")



root.mainloop()