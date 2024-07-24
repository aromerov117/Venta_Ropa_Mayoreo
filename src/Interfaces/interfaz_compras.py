import tkinter as tk
from tkinter import *


class Compras_ventana:
    def __init__(self, root, frame_contenedor):
        self.root = root
        self.frame_contenedor = frame_contenedor

    def limpiar_contenido(self):
        # Eliminar todos los widgets dentro del frame_contenedor
        for widget in self.frame_contenedor.winfo_children():
            widget.destroy()

    def compra_nuevo(self):
        self.limpiar_contenido()
        label_id_proveedor = tk.Label(self.frame_contenedor, text="Id Proveedor", bg='blue')
        label_id_proveedor.grid(row=0, column=0, padx=10, pady=10)
        cuadro_id_proveedor = tk.Entry(self.frame_contenedor)
        cuadro_id_proveedor.grid(row=0, column=1, padx=10, pady=10)

        label_id_producto = tk.Label(self.frame_contenedor, text="Id Producto", bg='blue')
        label_id_producto.grid(row=1, column=0, padx=10, pady=10)
        cuadro_id_producto = tk.Entry(self.frame_contenedor)
        cuadro_id_producto.grid(row=1, column=1, padx=10, pady=10)

        label_nombre_producto = tk.Label(self.frame_contenedor, text="Nombre", bg='blue')
        label_nombre_producto.grid(row=2, column=0, padx=10, pady=10)
        cuadro_nombre_producto = tk.Entry(self.frame_contenedor)
        cuadro_nombre_producto.grid(row=2, column=1, padx=10, pady=10)

        label_descripcion_producto = tk.Label(self.frame_contenedor, text="Descripcion", bg='blue')
        label_descripcion_producto.grid(row=3, column=0, padx=10, pady=10)
        cuadro_descripcion_producto = tk.Entry(self.frame_contenedor)
        cuadro_descripcion_producto.grid(row=3, column=1, padx=10, pady=10)

        label_talla_chica = tk.Label(self.frame_contenedor, text="Cantidad Talla Chica", bg='blue')
        label_talla_chica.grid(row=4, column=0, padx=10, pady=10)
        cuadro_talla_chica = tk.Entry(self.frame_contenedor)
        cuadro_talla_chica.grid(row=4, column=1, padx=10, pady=10)

        label_talla_mediana = tk.Label(self.frame_contenedor, text="Cantidad Talla Mediana", bg='blue')
        label_talla_mediana.grid(row=5, column=0, padx=10, pady=10)
        cuadro_talla_mediana = tk.Entry(self.frame_contenedor)
        cuadro_talla_mediana.grid(row=5, column=1, padx=10, pady=10)

        label_talla_grande = tk.Label(self.frame_contenedor, text="Cantidad Talla Grande", bg='blue')
        label_talla_grande.grid(row=6, column=0, padx=10, pady=10)
        cuadro_talla_grande = tk.Entry(self.frame_contenedor)
        cuadro_talla_grande.grid(row=6, column=1, padx=10, pady=10)

        label_color_producto = tk.Label(self.frame_contenedor, text="Color", bg='blue')
        label_color_producto.grid(row=7, column=0, padx=10, pady=10)
        cuadro_color_producto = tk.Entry(self.frame_contenedor)
        cuadro_color_producto.grid(row=7, column=1, padx=10, pady=10)

        label_precio_costo = tk.Label(self.frame_contenedor, text="Precio Costo", bg='blue')
        label_precio_costo.grid(row=8, column=0, padx=10, pady=10)
        cuadro_precio_costo = tk.Entry(self.frame_contenedor)
        cuadro_precio_costo.grid(row=8, column=1, padx=10, pady=10)

        label_precio_venta = tk.Label(self.frame_contenedor, text="Precio Venta", bg='blue')
        label_precio_venta.grid(row=9, column=0, padx=10, pady=10)
        cuadro_precio_venta = tk.Entry(self.frame_contenedor)
        cuadro_precio_venta.grid(row=9, column=1, padx=10, pady=10)

        boton_comprar = tk.Button(self.frame_contenedor, text="Comprar")
        boton_comprar.grid(row=0, column=3, padx=10, pady=10)



    def compra_existente(self):
        self.limpiar_contenido()

        label_id_producto = tk.Label(self.frame_contenedor, text="Id Producto", bg='blue')
        label_id_producto.grid(row=0, column=0, padx=10, pady=10)
        cuadro_Id_Producto = tk.Entry(self.frame_contenedor)
        cuadro_Id_Producto.grid(row=0, column=1, padx=10, pady=10)

        varTalla = IntVar()
        label_talla = tk.Label(self.frame_contenedor, text="Talla", bg='blue')
        label_talla.grid(row=2, column=0, padx=10, pady=10)

        radiobutton_chica = tk.Radiobutton(self.frame_contenedor, text="Chica", variable=varTalla, value=1)
        radiobutton_chica.grid(row=2, column=1, padx=10, pady=10)

        radiobutton_mediana = tk.Radiobutton(self.frame_contenedor, text="Mediana", variable=varTalla, value=2)
        radiobutton_mediana.grid(row=2, column=2, padx=10, pady=10)

        radiobutton_grande = tk.Radiobutton(self.frame_contenedor, text="Grande", variable=varTalla, value=3)
        radiobutton_grande.grid(row=2, column=3, padx=10, pady=10)

        label_cantidad = tk.Label(self.frame_contenedor, text="Cantidad", bg='blue')
        label_cantidad.grid(row=1, column=0, padx=10, pady=10)
        cuadro_cantidad = tk.Entry(self.frame_contenedor)
        cuadro_cantidad.grid(row=1, column=1, padx=10, pady=10)












