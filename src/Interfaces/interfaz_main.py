# interfaz_main.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from registro_usuario import registrar_usuario, visualizar_usuarios
from inicio_sesion import iniciar_sesion
from interfaz_catalogo import CatalogoWindow
from edicion_gestion_usuarios import *

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Ropa al Mayoreo")
        self.root.geometry("700x300")  # Tamaño estándar de la ventana
        self.center_window(self.root)  # Centrar ventana en la pantalla
        self.menuInicio()
        self.current_window = None

    def menuInicio(self):
        # Limpiar la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

        barraMenu = tk.Menu(self.root)
        root.config(menu=barraMenu)

        inicioSesionOpcion = tk.Menu(barraMenu, tearoff=0)
        inicioSesionOpcion.add_command(label="Iniciar Sesion", command=self.mostrar_inicio_sesion)

        registroOpcion = tk.Menu(barraMenu, tearoff=0)
        registroOpcion.add_command(label="Registrase", command=self.mostrar_registro)

        opcionesOpcion = tk.Menu(barraMenu, tearoff=0)
        opcionesOpcion.add_command(label="Salir", command=self.root.destroy)

        barraMenu.add_cascade(label="Inicio de Sesión", menu=inicioSesionOpcion)
        barraMenu.add_cascade(label="Registro", menu=registroOpcion)
        barraMenu.add_cascade(label="Opciones", menu=opcionesOpcion)

        tk.Label(root, text="Bienvenido", font=("Helvetica", 16)).pack(pady=20)
        #tk.Button(root, text="Registrarse", command=self.mostrar_registro).pack(pady=10)
        #tk.Button(root, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=10)

    def salirAplicacion(self, root):
        valor = messagebox.askokcancel('Salir', '¿Salir del programa?')
        if valor == True:
            root.destroy()

    def center_window(self, root):
        # Obtener el tamaño de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Calcular la posición del centro
        x_cordinate = int((screen_width/2) - (400/2))
        y_cordinate = int((screen_height/2) - (300/2))
        root.geometry(f"{400}x{300}+{x_cordinate}+{y_cordinate}")

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
        # Limpiar la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

        barraMenu = tk.Menu(self.root)
        root.config(menu=barraMenu)

        opcionesMenu = tk.Menu(barraMenu, tearoff=0)
        opcionesMenu.add_command(label="Volver", command=self.menuInicio)

        barraMenu.add_cascade(label="Opciones", menu=opcionesMenu)

        # Añadir widgets para la pantalla de inicio de sesión
        tk.Label(self.root, text="Correo electrónico:").grid(row=0, column=0, padx=10, pady=5)
        self.correo_entry = tk.Entry(self.root)
        self.correo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.contrasena_entry = tk.Entry(self.root, show="*")
        self.contrasena_entry.grid(row=1, column=1, padx=10, pady=5)

        iniciar_btn = tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion)
        iniciar_btn.grid(row=2, columnspan=2, pady=10)

    def iniciar_sesion(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()

        iniciado, mensaje = iniciar_sesion(correo, contrasena)
        if iniciado:
            messagebox.showinfo("Inicio de Sesión", mensaje)
            self.close_current_window()
            self.mostrar_menu2()
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

    def mostrar_menu2(self):
        # Limpiar la ventana actual
        for widget in self.root.winfo_children():
            widget.destroy()

        barraMenu = tk.Menu(self.root)
        self.root.config(menu=barraMenu, width=300, height=300)

        # Menú Catalogo
        catalogoMenu = tk.Menu(barraMenu, tearoff=0)
        catalogoMenu.add_command(label="Productos")
        # Menú Compras
        comprasMenu = tk.Menu(barraMenu, tearoff=0)
        comprasMenu.add_command(label="Realizar Compra")
        # Menú Salir
        salirMenu = tk.Menu(barraMenu, tearoff=0)
        salirMenu.add_command(label="Cerrar Sesión", command=self.menuInicio)

        barraMenu.add_cascade(label="Catalogo", menu=catalogoMenu)
        barraMenu.add_cascade(label="Compras", menu=comprasMenu)
        barraMenu.add_cascade(label="Ventas", menu=comprasMenu)
        barraMenu.add_cascade(label="Devoluciones", menu=comprasMenu)
        barraMenu.add_cascade(label="Proveedores", menu=comprasMenu)
        barraMenu.add_cascade(label="Inventario", menu=comprasMenu)
        barraMenu.add_cascade(label="Análisis Contable", menu=comprasMenu)
        barraMenu.add_cascade(label="Salir", menu=salirMenu)

    def seleccionar_opcion(self, opcion_index):
        if opcion_index == 0:
            CatalogoWindow(self).cargar_productos()



if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
