import tkinter as tk
from tkinter import ttk
from registro_producto import productos_registrados


class CatalogoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Productos")  # Esto funciona solo si root es un objeto Tk
        #self.root.geometry("800x400")  # Tamaño estándar de la ventana
        #self.center_window(self.root)  # Centrar ventana en la pantalla

        # Limpiar la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear un marco principal para el contenido del catálogo
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear un lienzo para el scroll horizontal
        self.canvas = tk.Canvas(main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear una barra de desplazamiento horizontal
        self.h_scrollbar = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear un marco para el contenido del catálogo
        self.catalog_frame = tk.Frame(self.canvas)

        # Añadir el marco al lienzo
        self.canvas.create_window((0, 0), window=self.catalog_frame, anchor="nw")

        # Vincular el marco al lienzo para actualizar el área de desplazamiento
        self.catalog_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.configure(xscrollcommand=self.h_scrollbar.set)

        # Crear una tabla para mostrar el catálogo de productos
        columns = (
            "ID", "Nombre", "Descripción", "Talla Chica", "Talla Mediana", "Talla Grande", "Color", "Precio Costo",
            "Precio Venta", "ID Proveedor")
        self.treeview = ttk.Treeview(self.catalog_frame, columns=columns, show="headings")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Definir encabezados de las columnas
        for col in columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, anchor="w")

        # Cargar los productos en la tabla
        self.cargar_productos()

    def center_window(self, window):
        window.update_idletasks()  # Actualiza las tareas pendientes de la ventana
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def on_frame_configure(self, event):
        # Actualizar el área de desplazamiento del lienzo
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def cargar_productos(self):
        for producto in productos_registrados:
            self.treeview.insert("", tk.END, values=(
                producto.id_producto,
                producto.nombre,
                producto.descripcion,
                producto.tallachica,
                producto.tallamediana,
                producto.tallagrande,
                producto.color,
                f"${producto.preciocosto:.2f}",
                f"${producto.precioventa:.2f}",
                producto.id_proveedor
            ))
