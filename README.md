# Lista de Tareas (Tkinter)

**Autor:** Leonardo Benjamín Córdova Jaramillo
**Universidad:** Universidad Estatal Amazónica (UEA)
**Materia:** Programación Orientada a Objetos (POO)
**Herramientas:** PyCharm, Python 3.14, Tkinter, pyinstaller

# Novedades: Semana 16 - Interacción Avanzada

En esta versión se han incorporado **atajos de teclado (shortcuts)** para mejorar la usabilidad y accesibilidad del sistema, permitiendo gestionar las tareas sin necesidad de usar el mouse exclusivamente.

### Atajos de Teclado Implementados:
- **`Enter`**: Añadir una nueva tarea una vez escrita la descripción.
- **`C` / `c`**: Marcar la tarea seleccionada como **Completada** (se vuelve verde).
- **`D` / `d` o `Delete`**: **Eliminar** la tarea seleccionada tras confirmación.
- **`Escape`**: **Cerrar** la aplicación solicitando una confirmación de salida.

### Mejoras Técnicas:
- **Evento de Doble Clic**: Se mantiene la funcionalidad de doble clic sobre una tarea para marcarla como completada.
- **Gestión de Foco**: Mejora en la fluidez de entrada de datos al permitir añadir tareas con Enter.
- **Validación Robusta**: Se evitan mensajes de advertencia intrusivos al usar atajos de teclado sin elementos seleccionados, mejorando la experiencia de usuario (UX).
- **Código Documentado**: Se han añadido comentarios y docstrings para facilitar la lectura y el mantenimiento siguiendo las buenas prácticas de Python.

---

### Estructura de Capas (Evolución)
Se mantiene estrictamente la arquitectura modular:
1. **`modelos/`**: Clase `Tarea` (datos puros).
2. **`servicios/`**: Lógica de gestión CRUD (procesamiento).
3. **`ui/`**: Interfaz con **Tkinter** y manejo avanzado de eventos `bind()`.
4. **`main.py`**: Inyección de dependencias y arranque del sistema.