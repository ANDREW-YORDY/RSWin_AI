"""
Servicio para captura de pantalla
"""
from tkinter import messagebox
import mss
import mss.tools
import os
from datetime import datetime


class ScreenshotService:

    """Servicio para manejar capturas de pantalla."""
    
    def __init__(self):
        self.output_path = "src/assets/img/screenshots"
        self.ensure_output_directory()
    
    def ensure_output_directory(self):
        """Crear directorio de salida si no existe."""
        os.makedirs(self.output_path, exist_ok=True)
    
    def capture_area(self, top=160, left=160, width=160, height=135):
        """Capturar área específica de la pantalla."""
        try:
            with mss.mss() as sct:
                # Configurar monitor
                monitor = {
                    "top": top, 
                    "left": left, 
                    "width": width, 
                    "height": height
                }
                
                # Generar nombre único
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_area_{timestamp}.png"
                output_file = os.path.join(self.output_path, filename)
                
                # Capturar
                sct_img = sct.grab(monitor)
                mss.tools.to_png(sct_img.rgb, sct_img.size, output=output_file)
                
                print(f"✓ Captura guardada: {output_file}")
                messagebox.showinfo("Éxito", f"Captura guardada como:\n{filename}")
                return output_file
                
        except Exception as e:
            print(f"✗ Error en captura: {e}")
            messagebox.showerror("Error", f"Error capturando pantalla: {e}")
            return None
    
    def capture_fullscreen(self):
        """Capturar pantalla completa."""
        try:
            with mss.mss() as sct:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"screenshot_full_{timestamp}.png"
                output_file = os.path.join(self.output_path, filename)
                
                sct.shot(output=output_file)
                
                print(f"✓ Captura completa guardada: {output_file}")
                messagebox.showinfo("Éxito", f"Captura completa guardada como:\n{filename}")
                return output_file
                
        except Exception as e:
            print(f"✗ Error en captura completa: {e}")
            messagebox.showerror("Error", f"Error capturando pantalla completa: {e}")
            return None


# from tkinter import messagebox, ttk
# import mss
# import mss.tools


# class ScreenshotService():

#     """Servicio para manejar capturas de pantalla."""

#     def __init__(self):
#         pass


#     with mss.mss() as sct:
#         #The screen part to capture.
#         monitor = { "top": 160, "left": 160, "width": 160, "height": 135 }
#         output  = "IMG_ESPECIFICA_sct-{top}x{left}_{width}x{height}.png".format(**monitor)

#         #Grab the data.
#         sct_img = sct.grab(monitor)

#         #Save to the picture file.
#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#         print(output)


#     # Scrennshot Full Screen.
#     # with mss.mss() as sct:
#     #     filename = sct.shot(output="captura_actual.png")
#     #     print(f"Captura guardada como {filename}")
