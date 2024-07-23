# interfaz_main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from registro_usuario import registrar_usuario, visualizar_usuarios
from inicio_sesion import iniciar_sesion
from interfaz_catalogo import mostrar_catalogo
from edicion_gestion_usuarios import *

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Ropa al Mayoreo")
        self.root.geometry("400x300")  # Tamaño estándar de la ventana
        self.center_window(self.root)  # Centrar ventana en la pantalla

        self.current_window = None

        tk.Label(root, text="Bienvenido", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(root, text="Registrarse", command=self.mostrar_registro).pack(pady=10)
        tk.Button(root, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=10)

    def center_window(self, window):
        window.update_idletasks()  # Actualiza las tareas pendientes de la ventana
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def close_current_window(self):
        if self.current_window:
            self.current_window.destroy()
            self.current_window = None

    def mostrar_registro(self):
        self.close_current_window()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Registro de Usuario")
        self.current_window.geometry("400x300")

        self.center_window(self.current_window)  # Centrar ventana secundaria

        tk.Label(self.current_window, text="Nombre completo:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(self.current_window)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.current_window, text="Correo electrónico:").grid(row=1, column=0, padx=10, pady=5)
        self.correo_entry = tk.Entry(self.current_window)
        self.correo_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.current_window, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5)
        self.telefono_entry = tk.Entry(self.current_window)
        self.telefono_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.current_window, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5)
        self.contrasena_entry = tk.Entry(self.current_window, show="*")
        self.contrasena_entry.grid(row=3, column=1, padx=10, pady=5)

        registrar_btn = tk.Button(self.current_window, text="Registrar", command=self.registrar_usuario)
        registrar_btn.grid(row=4, columnspan=2, pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        contrasena = self.contrasena_entry.get()

        registrado, mensaje = registrar_usuario(nombre, correo, telefono, contrasena)
        messagebox.showinfo("Registro de Usuario", mensaje)

        if registrado:
            self.close_current_window()
            self.mostrar_menu()

    def mostrar_inicio_sesion(self):
        self.close_current_window()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Inicio de Sesión")
        self.current_window.geometry("400x300")

        self.center_window(self.current_window)  # Centrar ventana secundaria

        tk.Label(self.current_window, text="Correo electrónico:").grid(row=0, column=0, padx=10, pady=5)
        self.correo_entry = tk.Entry(self.current_window)
        self.correo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.current_window, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.contrasena_entry = tk.Entry(self.current_window, show="*")
        self.contrasena_entry.grid(row=1, column=1, padx=10, pady=5)

        iniciar_btn = tk.Button(self.current_window, text="Iniciar Sesión", command=self.iniciar_sesion)
        iniciar_btn.grid(row=2, columnspan=2, pady=10)

    def iniciar_sesion(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()

        iniciado, mensaje = iniciar_sesion(correo, contrasena)
        if iniciado:
            messagebox.showinfo("Inicio de Sesión", mensaje)
            self.close_current_window()
            self.mostrar_menu()
        else:
            messagebox.showerror("Inicio de Sesión", mensaje)

    def mostrar_menu(self):
        self.close_current_window()
        self.current_window = tk.Toplevel(self.root)
        self.current_window.title("Menú Principal")
        self.current_window.geometry("600x400")

        self.center_window(self.current_window)  # Centrar ventana secundaria

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

        opciones_combobox = ttk.Combobox(self.current_window, values=opciones_menu, state="readonly")
        opciones_combobox.grid(row=0, column=0, padx=10, pady=10)

        seleccionar_btn = tk.Button(self.current_window, text="Seleccionar",
                                    command=lambda: self.seleccionar_opcion(opciones_combobox.current()))
        seleccionar_btn.grid(row=0, column=1, padx=10, pady=10)

    def seleccionar_opcion(self, opcion_index):
        if opcion_index == 0:
            mostrar_catalogo()


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
