"""
main.py
Punto de entrada principal de la aplicación Lista de Tareas.

Autor: Leonardo Benjamín Córdova Jaramillo
Universidad: Universidad Estatal Amazónica (UEA)
Materia: Programación Orientada a Objetos (POO)
Python: 3.15
"""

import sys
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTareas


def configurar_resolucion():
    """Mejora la nitidez en pantallas de alta resolución (Windows)."""
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass


def main():
    """Inicializa el servicio e inyecta la dependencia en la interfaz."""
    configurar_resolucion()
    servicio = TareaServicio()
    try:
        app = AppTareas(servicio)
        app.mainloop()
    except Exception as e:
        print(f"Error crítico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()