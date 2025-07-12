# """
# PUNTO DE ENTRADA GLOBAL DE TODA LA APLICACIÓN
# """
# import sys
# import os

# # Agregar src al path para importaciones
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# from view.gui.screenshot import AppScreenshot
# # from otros_modulos import OtroModulo  # Aquí importarías otros módulos

# class MainApp:
#     """Clase principal de toda la aplicación."""
    
#     def __init__(self):
#         self.current_module = None
#         self.setup_main_menu()
    
#     def setup_main_menu(self):
#         """Configurar menú principal de la aplicación."""
#         print("=" * 50)
#         print("🎯 RSWIN AI - APLICACIÓN PRINCIPAL")
#         print("=" * 50)
#         print("Selecciona un módulo:")
#         print("1. Screenshot")
#         print("2. Otro módulo (futuro)")
#         print("0. Salir")
#         print("=" * 50)
    
#     def run(self):
#         """Ejecutar la aplicación principal."""
#         while True:
#             self.setup_main_menu()
#             choice = input("Selecciona una opción: ")
            
#             if choice == "1":
#                 self.run_screenshot_module()
#             elif choice == "2":
#                 print("⚠️  Módulo aún no implementado")
#             elif choice == "0":
#                 print("👋 Cerrando aplicación...")
#                 break
#             else:
#                 print("❌ Opción no válida")
    
#     def run_screenshot_module(self):
#         """Ejecutar módulo de screenshot."""
#         print("🚀 Cargando módulo Screenshot...")
#         app = AppScreenshot()
#         app.run()

# # PUNTO DE ENTRADA PRINCIPAL
# if __name__ == "__main__":
#     print("🎯 Iniciando RSWIN AI - Aplicación Global")
#     main_app = MainApp()
#     main_app.run()
