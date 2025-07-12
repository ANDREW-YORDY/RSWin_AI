"""
Clase para manejo de archivos e imágenes
"""
# FilePath de la la imagen capturada. Clase para guardar el screenshot en una ruta especifica, dentro del proyecto.
# Tmbien, se redimensiona la imagen.

from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

class FileImg:
    """Clase para manejar archivos e imágenes."""
    
    def __init__(self):
        self.base_path = "src/assets/img"
        self.screenshots_path = os.path.join(self.base_path, "screenshots")
        self.ensure_directories()
    
    def ensure_directories(self):
        """Crear directorios si no existen."""
        os.makedirs(self.screenshots_path, exist_ok=True)
    
    def test_message(self):
        """Mostrar mensaje de prueba."""
        messagebox.showinfo("Información", "Iniciando capturas de pantalla")
    
    def test_pil(self, root):
        """Cargar y mostrar imagen usando PIL."""
        try:
            imagen_path = os.path.join(self.base_path, "Gyomei_himejima.png")
            imagen = Image.open(imagen_path)
            
            # Redimensionar tamaño de la imagen original
            imagen.thumbnail((540, 500), Image.Resampling.LANCZOS)
            image_tk = ImageTk.PhotoImage(imagen)
            
            # Crear o actualizar label de imagen
            if hasattr(root, 'label_img'):
                root.label_img.configure(image=image_tk)
                root.label_img.image = image_tk
            else:
                root.label_img = ttk.Label(root, image=image_tk)
                root.label_img.image = image_tk
                root.label_img.place(x=350, y=90)
            
            print("✓ Imagen cargada correctamente")
            
        except FileNotFoundError:
            print("✗ No se encontró la imagen")
            messagebox.showerror("Error", "No se encontró la imagen.")
        except Exception as e:
            print(f"✗ Error: {e}")
            messagebox.showerror("Error", f"Error cargando imagen: {e}")




# class FileImg():

#     def __init__(self):
#         pass
    

#     def testMessahge():
#         """Mostrar mensaje de prueba."""
#         messagebox.showinfo("Iniciar capturas de pantalla")

#     def test_pil(self, root):
#         """Cargar y mostrar imagen usando PIL"""

#         try:

#             imagen = Image.open("src/assets/img/Gyomei_himejima.png")
#             # Reimensionar tamaño de la img oroginal.
#             imagen.thumbnail((540, 500), Image.Resampling.LANCZOS)
#             Image_Tk = ImageTk.PhotoImage(imagen)

#             label_img = ttk.Label(root, image=Image_Tk)
#             label_img.image = Image_Tk
#             # Ubicando la posición dedel label de la img.
#             label_img.place(x=350, y=90)

#             print("✓ Imagen cargada correctamente")

#         except FileNotFoundError:
#             print("✗ No se encontró la imagen")
#             messagebox.showerror("Error", "No se encontró la Imagen.")
#         except Exception as e:
#             print(f"✗ Error: {e}")
#             messagebox.showerror("Error", f"Error cargando imagen: {e}")
