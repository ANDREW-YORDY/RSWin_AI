# Clase que diseña y establece propiedades a las interfaces gráficas UI.
"""
Clase para componentes de la interfaz gráfica
"""

from tkinter import ttk
# from view.gui.screenshot.fileImg import Functions
# from fileImg import test_pil, testMessahge


class GuiComponents:

    """Clase para crear componentes de la interfaz de usuario."""

    def __init__(self, fileService, scService):
        self.fileService = fileService
        self.scService = scService

    def fnGuiComponents(self, root):
        """Crear todos los elementos de la interfaz de usuario"""

        # ttk.Label(frm, text="SCREENSHOT").grid(column=0, row=0)
        # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        titleLabel = ttk.Label(root, text="PreView", font=("Arial", 16, "bold"))
        titleLabel.place(x=600, y=50)


        # Botón para iniciar screenshot
        btnStart = ttk.Button(
            root, text="START SCREENSHOT",
            padding=20, 
            width=40,
            command=lambda: self.fileService.test_pil(root)
        )
        btnStart.place(x=50, y=100)

        # Botón para preview screenshot
        btnView = ttk.Button(
            root, text="PREVIEW SCREENSHOT",
            padding=20, 
            width=40,
            command=lambda: self.fileService.test_pil(root)
        )
        btnView.place(x=50, y=190)


        # Botón para mensaje de prueba
        btn_screenshot = ttk.Button(
            root, 
            text="GO SCRENNSHOT",
            padding=20, 
            width=40,
            command=lambda: self.scService.capture_area()
        )
        btn_screenshot.place(x=50, y=280)
