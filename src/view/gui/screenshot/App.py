# Clase principal, main. La cual ejecuta el modulo ó paquete de "screenshot". Desde esta clase se ejecuta y muestra la interfaz princoal, temporalmente.

import tkinter as tk
from tkinter import *
from tkinter import ttk
from Filelmg import FileImg
from GuiComponents import GuiComponents
from ScreenshotService import  ScreenshotService
#from view.gui.screenshot.Gui_Elements import GuiComponents  --> Incorrecto


# DEBO ESTABLECER ESTA CLASE COMO LA CLASE MAIN DEL MODULO screenshot.

class AppScreenshot:

    """Clase principal del módulo screenshot."""

    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.geometry("900x650")
        self.root.title("SCREENSHOT")

        # instanciar servicios de la clase FileImg().
        self.fileImg = FileImg()
        # instanciar servicios de la clase ScreeshotService().
        self.scsService = ScreenshotService()


        # Crear componentes GUI.
        self.gui = GuiComponents(self.fileImg, self.scsService)
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
        print("🚀 Iniciando módulo Screenshot...")
        self.root.mainloop()



# root.mainloop()
