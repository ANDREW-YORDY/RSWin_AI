from tkinter import ttk
from fileImg import test_pil




def fnGuiElements(root):
    """Crear todos los elementos de la interfaz de usuario"""

    # ttk.Label(frm, text="SCREENSHOT").grid(column=0, row=0)
    # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    titleLabel = ttk.Label(root, text="PreView")
    titleLabel.place(x=600, y=50)

    btnStart = ttk.Button(
        root, text="START", 
        padding=20, width=20,
        command=lambda: test_pil(root)
        ).place(x=50, y=100)

    btnView  = ttk.Button(
        root, text="PREVIEW SCREENSHOT", 
        padding=20, width=20,
        command=lambda: test_pil(root)
        ).place(x=50, y=190)
