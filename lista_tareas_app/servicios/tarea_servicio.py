"""
tarea_servicio.py
Capa de Servicio: lógica de negocio para gestionar la lista de tareas.

Autor: Leonardo Benjamín Córdova Jaramillo
Universidad: Universidad Estatal Amazónica (UEA)
"""

from modelos.tarea import Tarea


class TareaServicio:
    """Gestiona la colección de tareas en memoria."""

    def __init__(self):
        self._tareas: list[Tarea] = []
        self._contador_id = 1

    def agregar_tarea(self, descripcion: str) -> Tarea | None:
        """Agrega una nueva tarea. Retorna None si la descripción está vacía."""
        descripcion = descripcion.strip()
        if not descripcion:
            return None
        tarea = Tarea(self._contador_id, descripcion)
        self._tareas.append(tarea)
        self._contador_id += 1
        return tarea

    def obtener_todas(self) -> list[Tarea]:
        """Retorna todas las tareas registradas."""
        return list(self._tareas)

    def completar_tarea(self, id: int) -> bool:
        """Marca como completada la tarea con el id dado."""
        for t in self._tareas:
            if t.get_id() == id:
                t.marcar_completada()
                return True
        return False

    def eliminar_tarea(self, id: int) -> bool:
        """Elimina la tarea con el id dado."""
        for t in self._tareas:
            if t.get_id() == id:
                self._tareas.remove(t)
                return True
        return False