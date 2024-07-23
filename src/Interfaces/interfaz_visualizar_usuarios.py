import tkinter as tk
from tkinter import ttk
from registro_usuario import usuarios_registrados

class VisualizarUsuariosWindow:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Visualizar Usuarios")
        self.parent.geometry("800x350")
        self.center_window()

        # Crear un marco principal para el contenido de los usuarios
        main_frame = tk.Frame(self.parent)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear un lienzo para el scroll horizontal
        self.canvas = tk.Canvas(main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear una barra de desplazamiento horizontal
        self.h_scrollbar = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear un marco para el contenido de los usuarios
        self.users_frame = tk.Frame(self.canvas)

        # Añadir el marco al lienzo
        self.canvas.create_window((0, 0), window=self.users_frame, anchor="nw")

        # Vincular el marco al lienzo para actualizar el área de desplazamiento
        self.users_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.configure(xscrollcommand=self.h_scrollbar.set)

        # Crear una tabla para mostrar los usuarios
        columns = ("Nombre Completo", "Correo Electrónico", "Teléfono", "Rol")
        self.treeview = ttk.Treeview(self.users_frame, columns=columns, show="headings")

        # Configuración de las columnas
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor="center", width=200)  # Ancho aumentado y centrado

        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Cargar los usuarios en la tabla
        self.cargar_usuarios()

    def on_frame_configure(self, event):
        # Actualizar el área de desplazamiento del lienzo
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def cargar_usuarios(self):
        for usuario in usuarios_registrados:
            self.treeview.insert("", tk.END, values=(
                usuario.nombre_completo,
                usuario.correo_electronico,
                usuario.telefono,
                usuario.rol
            ))

    def center_window(self):
        # Centrar la ventana en la pantalla
        self.parent.update_idletasks()
        window_width = self.parent.winfo_width()
        window_height = self.parent.winfo_height()
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.parent.geometry(f'{window_width}x{window_height}+{x}+{y}')
