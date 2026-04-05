# Lista de Tareas (Tkinter)

**Autor:** Leonardo Benjamín Córdova Jaramillo
**Universidad:** Universidad Estatal Amazónica (UEA)
**Materia:** Programación Orientada a Objetos (POO)
**Herramientas:** PyCharm, Python 3.14, Tkinter, pyinstaller

## Descripción
Aplicación de escritorio modular para gestionar tareas diarias. Desarrollada con arquitectura por capas (Modelo, Servicio, UI) aplicando principios de POO y manejo de eventos con Tkinter.

## Estructura de carpetas
```text
lista_tareas_app/
├── main.py
├── modelos/
│   ├── __init__.py
│   └── tarea.py
├── servicios/
│   ├── __init__.py
│   └── tarea_servicio.py
└── ui/
    ├── __init__.py
    └── app_tkinter.py
```

## Funcionalidades
Añadir tarea: Escribir descripción y presionar el botón o la tecla Enter.
Estado visual: Tareas pendientes en rojo, completadas en azul.
Marcar completada: Botón o doble clic sobre la tarea.
Eliminar: Con mensaje de confirmación previa.
Campo vacío: No permite agregar tareas sin descripción.
Cierre seguro: Confirmación al cerrar la ventana.
Tooltips: Descripción breve al pasar el mouse sobre cada botón.

# #Principios POO Aplicados
Encapsulamiento: Atributos privados en la clase Tarea.
Abstracción: TareaServicio oculta la lógica a la interfaz.
Herencia: AppTareas hereda de tk.Tk.
Inyección de Dependencias: El servicio se inyecta desde main.py.