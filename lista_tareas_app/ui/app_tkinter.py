"""
app_tkinter.py
Capa UI: interfaz gráfica de la Lista de Tareas con manejo de eventos.

Autor: Leonardo Benjamín Córdova Jaramillo
Universidad: Universidad Estatal Amazónica (UEA)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from servicios.tarea_servicio import TareaServicio


class AppTareas(tk.Tk):
    """Ventana principal de la aplicación Lista de Tareas."""

    def __init__(self, servicio: TareaServicio):
        super().__init__()
        self.servicio = servicio
        self.title("Lista de Tareas")
        self.geometry("700x450")
        self.resizable(True, True)
        self.configure(bg="#f0f3f5")

        # Interceptar el cierre de ventana para pedir confirmación (Click en X)
        self.protocol("WM_DELETE_WINDOW", self._confirmar_cierre)

        self._crear_componentes()

    # ------------------------------------------------------------------ #
    #  INTERFAZ                                                            #
    # ------------------------------------------------------------------ #

    def _crear_componentes(self):
        """Construye todos los widgets de la interfaz."""

        # HEADER
        header = tk.Frame(self, bg="#1a2a3a")
        header.pack(fill="x")
        tk.Label(header, text="LISTA DE TAREAS",
                 font=("Segoe UI", 16, "bold"),
                 fg="white", bg="#1a2a3a").pack(pady=8)

        # ENTRADA DE TEXTO
        entrada_frame = tk.Frame(self, bg="#f0f3f5", pady=10)
        entrada_frame.pack(fill="x", padx=20)

        tk.Label(entrada_frame, text="Nueva tarea:",
                 bg="#f0f3f5", font=("Arial", 10)).pack(side="left", padx=(0, 8))

        self.entry_tarea = tk.Entry(entrada_frame, font=("Arial", 11),
                                    relief="solid", bd=1, width=45)
        self.entry_tarea.pack(side="left", padx=(0, 10))

        # Evento de teclado: Enter agrega la tarea (Ya existente)
        self.entry_tarea.bind("<Return>", lambda e: self._agregar_tarea())

        # BOTONES
        btn_frame = tk.Frame(self, bg="#f0f3f5")
        btn_frame.pack(pady=5)

        self.btn_agregar = tk.Button(
            btn_frame, text="Añadir Tarea",
            bg="#27ae60", fg="white", font=("Arial", 9, "bold"),
            width=16, command=self._agregar_tarea)
        self.btn_agregar.pack(side="left", padx=6)

        self.btn_completar = tk.Button(
            btn_frame, text="Marcar Completada",
            bg="#2980b9", fg="white", font=("Arial", 9, "bold"),
            width=18, command=self._marcar_completada)
        self.btn_completar.pack(side="left", padx=6)

        self.btn_eliminar = tk.Button(
            btn_frame, text="Eliminar",
            bg="#e74c3c", fg="white", font=("Arial", 9, "bold"),
            width=12, command=self._eliminar_tarea)
        self.btn_eliminar.pack(side="left", padx=6)

        # Tooltips al pasar el mouse sobre los botones
        self._agregar_tooltip(self.btn_agregar, "TECLA ´ENTER´ - Añade tarea a la lista.")
        self._agregar_tooltip(self.btn_completar, "Tecla ´C´ - Marca tarea Completada.")
        self._agregar_tooltip(self.btn_eliminar, "Tecla ´D´ - Elimina una tarea del listado.")

        # TABLA (Treeview)
        tabla_frame = tk.Frame(self, bg="#f0f3f5")
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)

        cols = ("id", "descripcion", "estado")
        self.tabla = ttk.Treeview(tabla_frame, columns=cols, show="headings")

        self.tabla.heading("id", text="ID")
        self.tabla.heading("descripcion", text="Descripción")
        self.tabla.heading("estado", text="Estado")

        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("descripcion", width=400, anchor="w")
        self.tabla.column("estado", width=120, anchor="center")

        # Colores por estado: rojo=pendiente, verde=completada (Semana 16)
        self.tabla.tag_configure("pendiente", foreground="white", background="#e74c3c")
        self.tabla.tag_configure("completada", foreground="white", background="#27ae60")

        scroll = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Evento de ratón: doble clic marca como completada
        self.tabla.bind("<Double-1>", lambda e: self._marcar_completada())

        # ------------------------------------------------------------------ #
        #  ATAJOS DE TECLADO (NUEVO SEMANA 16)                               #
        # ------------------------------------------------------------------ #

        # Cerrar app con Escape
        self.bind("<Escape>", lambda e: self._confirmar_cierre())

        # Marcar completada con 'C' o 'c'
        self.bind("<KeyPress-c>", lambda e: self._marcar_completada())
        self.bind("<KeyPress-C>", lambda e: self._marcar_completada())

        # Eliminar con 'D', 'd' o la tecla 'Delete' (Supr)
        self.bind("<KeyPress-d>", lambda e: self._eliminar_tarea())
        self.bind("<KeyPress-D>", lambda e: self._eliminar_tarea())
        self.bind("<Delete>", lambda e: self._eliminar_tarea())

    # ------------------------------------------------------------------ #
    #  TOOLTIP                                                             #
    # ------------------------------------------------------------------ #

    def _agregar_tooltip(self, widget, texto: str):
        """Muestra un mensaje breve al pasar el mouse sobre un botón."""
        tooltip = tk.Toplevel(widget)
        tooltip.withdraw()
        tooltip.overrideredirect(True)
        label = tk.Label(tooltip, text=texto, bg="#ffffe0",
                         font=("Arial", 8), relief="solid", bd=1, padx=4, pady=2)
        label.pack()

        def mostrar(event):
            x = widget.winfo_rootx() + 20
            y = widget.winfo_rooty() + widget.winfo_height() + 4
            tooltip.geometry(f"+{x}+{y}")
            tooltip.deiconify()

        def ocultar(event):
            tooltip.withdraw()

        widget.bind("<Enter>", mostrar)
        widget.bind("<Leave>", ocultar)

    # ------------------------------------------------------------------ #
    #  LÓGICA DE BOTONES                                                   #
    # ------------------------------------------------------------------ #

    def _agregar_tarea(self):
        """Agrega una nueva tarea. No permite descripción vacía."""
        descripcion = self.entry_tarea.get().strip()
        if not descripcion:
            messagebox.showwarning("Campo vacío",
                                   "Debes escribir una descripción para la tarea.")
            return

        tarea = self.servicio.agregar_tarea(descripcion)
        if tarea:
            self.entry_tarea.delete(0, tk.END)
            self._refrescar_tabla()

    def _marcar_completada(self):
        """Marca la tarea seleccionada como completada y cambia su color."""
        sel = self.tabla.selection()
        if not sel:
            return  # No mostrar warning en atajo de teclado para no molestar

        id_tarea = int(self.tabla.set(sel[0], "id"))
        if self.servicio.completar_tarea(id_tarea):
            self._refrescar_tabla()

    def _eliminar_tarea(self):
        """Elimina la tarea seleccionada con confirmación previa."""
        sel = self.tabla.selection()
        if not sel:
            return  # No mostrar warning en atajo de teclado para no molestar

        id_tarea = int(self.tabla.set(sel[0], "id"))
        descripcion = self.tabla.set(sel[0], "descripcion")

        if messagebox.askyesno("Confirmar eliminación",
                               f"¿Deseas eliminar la tarea:\n'{descripcion}'?"):
            if self.servicio.eliminar_tarea(id_tarea):
                self._refrescar_tabla()

    def _confirmar_cierre(self):
        """Pide confirmación antes de cerrar la ventana."""
        if messagebox.askyesno("Salir",
                               "¿Estás seguro de que deseas cerrar la aplicación?"):
            self.destroy()

    # ------------------------------------------------------------------ #
    #  TABLA                                                               #
    # ------------------------------------------------------------------ #

    def _refrescar_tabla(self):
        """Recarga la tabla con todas las tareas del servicio."""
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for t in self.servicio.obtener_todas():
            tag = "completada" if t.is_completada() else "pendiente"
            self.tabla.insert("", "end",
                              iid=str(t.get_id()),
                              values=(t.get_id(), t.get_descripcion(), t.get_estado()),
                              tags=(tag,))