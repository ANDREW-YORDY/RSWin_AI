"""
Módulo Screenshot - Punto de entrada del paquete
"""

from App import AppScreenshot

__all__ = ['AppScreenshot']


if __name__ == "__main__":
    app = AppScreenshot()
    app.run()