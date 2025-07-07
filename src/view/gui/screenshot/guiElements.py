from tkinter import ttk
# from view.gui.screenshot.fileImg import Functions
# from fileImg import test_pil, testMessahge


class GuiComponents():

    def __init__(self, fn):
        self.fn = fn

    def fnGuiComponents(self, root):
        """Crear todos los elementos de la interfaz de usuario"""
        # root.fn = fn

        # ttk.Label(frm, text="SCREENSHOT").grid(column=0, row=0)
        # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        titleLabel = ttk.Label(root, text="PreView")
        titleLabel.place(x=600, y=50)

        btnStart = ttk.Button(
            root, text="START SCREENSHOT",
            padding=20, width=20,
            command=lambda: self.fn.test_pil(root)
        )
        btnStart.place(x=50, y=100)

        btnView = ttk.Button(
            root, text="PREVIEW SCREENSHOT",
            padding=20, width=20,
            command=lambda: self.fn.test_pil(root)
        )
        btnView.place(x=50, y=190)
