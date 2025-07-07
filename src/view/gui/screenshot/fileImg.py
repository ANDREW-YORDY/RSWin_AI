from tkinter import messagebox, ttk
from PIL import Image, ImageTk


class Functions:

    def __init__(self):
        pass

    def testMessahge():
        """Mostrar mensaje de prueba."""
        messagebox.showinfo("Iniciar capturas de pantalla")

    def test_pil(self, root):
        """Cargar y mostrar imagen usando PIL"""

        try:

            imagen = Image.open("src/assets/img/Gyomei_himejima.png")
            # Reimensionar tamaño de la img oroginal.
            imagen.thumbnail((540, 500), Image.Resampling.LANCZOS)
            Image_Tk = ImageTk.PhotoImage(imagen)

            label_img = ttk.Label(root, image=Image_Tk)
            label_img.image = Image_Tk
            # Ubicando la posición dedel label de la img.
            label_img.place(x=350, y=90)

            print("✓ Imagen cargada correctamente")

        except FileNotFoundError:
            print("✗ No se encontró la imagen")
            messagebox.showerror("Error", "No se encontró la Imagen.")
        except Exception as e:
            print(f"✗ Error: {e}")
            messagebox.showerror("Error", f"Error cargando imagen: {e}")
