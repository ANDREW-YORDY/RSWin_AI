from tkinter import messagebox, ttk
from PIL import Image, ImageTk


# def testMessahge():
#     ven = messagebox.showinfo("Botón Start, Presionado.")

# def FnLabelImage():
#     ven = messagebox.showinfo("Botón Start, Ver Imagen.")


def test_pil(root):

    try:

        imagen = Image.open("src/assets/img/Gyomei_himejima.png")
        imagen.thumbnail((540,500), Image.Resampling.LANCZOS)
        Image_Tk = ImageTk.PhotoImage(imagen)

        label_img = ttk.Label(root, image=Image_Tk)
        label_img.image = Image_Tk
        label_img.place(x=350, y=90)

        print("✓ Imagen cargada correctamente")

    except FileNotFoundError:
        print("✗ No se encontró la imagen")
        messagebox.showerror("Error", "No se encontró la Imagen.")
    except Exception as e:
        print(f"✗ Error: {e}")
        messagebox.showerror("Error", f"Error cargando imagen: {e}")
