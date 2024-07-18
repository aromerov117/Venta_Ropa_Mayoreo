import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from registro_usuario import registrar_usuario, visualizar_usuarios
from inicio_sesion import iniciar_sesion
from ventas import mostrar_historial_ventas
from compras import mostrar_historial_compras
from contabilidad import mostrar_analisis_contabilidad
from catalogo import mostrar_catalogo
from compra_venta import *
from modelos import Producto
from gestion_proveedores import *
from edicion_gestion_usuarios import *
from registro_producto import Producto
from gestion_inventario import menu_gestion_inventario

class InterfazPrincipal:
    def __init__(self, root, opciones_menu):
        self.root = root
        self.opciones_menu = opciones_menu  # Guardar opciones_menu como atributo de instancia
        self.root.title("Sistema de Gestión de Ropa al Mayoreo")

        tk.Label(root, text="Bienvenido", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(root, text="Registrarse", command=self.interfaz_registro).pack(pady=5)
        tk.Button(root, text="Iniciar Sesión", command=self.interfaz_inicio_sesion).pack(pady=5)

    def interfaz_registro(self):
        registro_window = tk.Toplevel(self.root)
        registro_window.title("Registro de Usuario")

        tk.Label(registro_window, text="Nombre completo:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(registro_window)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(registro_window, text="Correo electrónico:").grid(row=1, column=0, padx=10, pady=5)
        self.correo_entry = tk.Entry(registro_window)
        self.correo_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(registro_window, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5)
        self.telefono_entry = tk.Entry(registro_window)
        self.telefono_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(registro_window, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5)
        self.contrasena_entry = tk.Entry(registro_window, show="*")
        self.contrasena_entry.grid(row=3, column=1, padx=10, pady=5)

        registrar_btn = tk.Button(registro_window, text="Registrar", command=self.registrar_usuario)
        registrar_btn.grid(row=4, columnspan=2, pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        contrasena = self.contrasena_entry.get()

        registrado, mensaje = registrar_usuario(nombre, correo, telefono, contrasena)
        messagebox.showinfo("Registro de Usuario", mensaje)

    def interfaz_inicio_sesion(self):
        inicio_sesion_window = tk.Toplevel(self.root)
        inicio_sesion_window.title("Inicio de Sesión")

        tk.Label(inicio_sesion_window, text="Correo electrónico:").grid(row=0, column=0, padx=10, pady=5)
        self.correo_entry = tk.Entry(inicio_sesion_window)
        self.correo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(inicio_sesion_window, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.contrasena_entry = tk.Entry(inicio_sesion_window, show="*")
        self.contrasena_entry.grid(row=1, column=1, padx=10, pady=5)

        iniciar_btn = tk.Button(inicio_sesion_window, text="Iniciar Sesión", command=self.iniciar_sesion)
        iniciar_btn.grid(row=2, columnspan=2, pady=10)

    def iniciar_sesion(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()

        iniciado, mensaje = iniciar_sesion(correo, contrasena)
        if iniciado:
            messagebox.showinfo("Inicio de Sesión", mensaje)
            self.mostrar_menu()
        else:
            messagebox.showerror("Inicio de Sesión", mensaje)

    def mostrar_menu(self):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Menú Principal")

        opciones_combobox = ttk.Combobox(menu_window, values=self.opciones_menu, state="readonly")
        opciones_combobox.grid(row=0, column=0, padx=10, pady=10)

        seleccionar_btn = tk.Button(menu_window, text="Seleccionar", command=self.seleccionar_opcion)
        seleccionar_btn.grid(row=0, column=1, padx=10, pady=10)

        self.opciones_combobox = opciones_combobox  # Guardar referencia como atributo de instancia

    def seleccionar_opcion(self):
        opcion_index = self.opciones_combobox.current()
        if opcion_index == 0:
            mostrar_catalogo()
        elif opcion_index == 1:
            menu_gestion_inventario()
        elif opcion_index == 2:
            # Funcionalidad para salida de productos
            pass
        elif opcion_index == 3:
            # Funcionalidad para devoluciones
            pass
        elif opcion_index == 4:
            menu_proveedores(proveedores)
        elif opcion_index == 5:
            menu_gestion_inventario()
        elif opcion_index == 6:
            mostrar_historial_ventas()
        elif opcion_index == 7:
            mostrar_historial_compras(compras_realizadas)
        elif opcion_index == 8:
            mostrar_analisis_contabilidad()
        elif opcion_index == 9:
            visualizar_usuarios()
        elif opcion_index == 10:
            editar_usuario()

if __name__ == "__main__":
    opciones_menu = [
        "Catalogo",
        "Entrada de Productos en Inventario",
        "Salida de Productos del Inventario",
        "Registro de Devoluciones de Productos al Proveedor",
        "Gestión de Proveedores y Contactos",
        "Gestión de Ajustes de Inventario",
        "Historial de Ventas",
        "Historial de Compras",
        "Análisis de Contabilidad de Compras y Ventas",
        "Visualizar usuarios",
        "Gestionar usuarios"
    ]

    root = tk.Tk()
    app = InterfazPrincipal(root, opciones_menu)
    root.mainloop()
