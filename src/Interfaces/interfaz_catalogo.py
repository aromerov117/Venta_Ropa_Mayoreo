# interfaz_catalogo.py

import tkinter as tk
from tkinter import ttk
from registro_producto import productos_registrados

class CatalogoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Productos")
        self.root.geometry("800x400")  # Tamaño estándar de la ventana
        self.center_window(self.root)  # Centrar ventana en la pantalla

        # Crear un marco para el contenido del catálogo
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Crear un lienzo (canvas) para el scroll horizontal
        canvas = tk.Canvas(frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Crear una barra de desplazamiento horizontal
        scrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear un marco en el lienzo para contener el árbol
        tree_frame = tk.Frame(canvas)

        # Crear un árbol (treeview) para mostrar los productos
        self.tree = ttk.Treeview(tree_frame, columns=(
        "Nombre", "Descripción", "Talla Chica", "Talla Mediana", "Talla Grande", "Color", "Precio Costo",
        "Precio Venta", "ID Proveedor"), show="headings", height=15)
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Talla Chica", text="Talla Chica")
        self.tree.heading("Talla Mediana", text="Talla Mediana")
        self.tree.heading("Talla Grande", text="Talla Grande")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Precio Costo", text="Precio Costo")
        self.tree.heading("Precio Venta", text="Precio Venta")
        self.tree.heading("ID Proveedor", text="ID Proveedor")

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Agregar el marco del árbol al lienzo y configurar el scroll
        canvas.create_window((0, 0), window=tree_frame, anchor="nw")
        tree_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.config(xscrollcommand=scrollbar.set)

        # Rellenar el árbol con los productos
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

    def cargar_productos(self):
        for producto in productos_registrados:
            self.tree.insert("", tk.END, values=(
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

def mostrar_catalogo():
    root = tk.Toplevel()  # Crear una ventana secundaria para el catálogo
    CatalogoWindow(root)
