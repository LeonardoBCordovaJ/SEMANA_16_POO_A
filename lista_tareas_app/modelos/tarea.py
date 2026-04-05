"""
tarea.py
Clase Tarea: representa una tarea de la lista con su id, descripción y estado.

Autor: Leonardo Benjamín Córdova Jaramillo
Universidad: Universidad Estatal Amazónica (UEA)
"""

class Tarea:
    """Modelo de datos para una tarea de la lista."""

    def __init__(self, id: int, descripcion: str):
        self._id = id
        self._descripcion = descripcion
        self._completada = False

    def get_id(self) -> int:
        return self._id

    def get_descripcion(self) -> str:
        return self._descripcion

    def is_completada(self) -> bool:
        return self._completada

    def marcar_completada(self):
        """Cambia el estado de la tarea a completada."""
        self._completada = True

    def get_estado(self) -> str:
        return "Completada" if self._completada else "Pendiente"