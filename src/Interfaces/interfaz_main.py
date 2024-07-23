import tkinter as tk
from tkinter import messagebox, ttk
from registro_usuario import registrar_usuario
from inicio_sesion import iniciar_sesion
from interfaz_catalogo import CatalogoWindow
from interfaz_visualizar_usuarios import VisualizarUsuariosWindow

class VentanaBienvenida:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenido")
        self.root.geometry("400x300")
        self.center_window(self.root)

        tk.Label(root, text="Bienvenido", font=("Helvetica", 16)).pack(pady=20)
        tk.Button(root, text="Registrarse", command=self.mostrar_registro).pack(pady=10)
        tk.Button(root, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=10)

    def center_window(self, window):
        window.update_idletasks()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def mostrar_registro(self):
        registro_window = tk.Toplevel(self.root)
        RegistroUsuario(registro_window)

    def mostrar_inicio_sesion(self):
        inicio_sesion_window = tk.Toplevel(self.root)
        InicioSesion(inicio_sesion_window)

class RegistroUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuario")
        self.root.geometry("400x300")
        self.center_window(self.root)

        tk.Label(root, text="Nombre completo:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Correo electrónico:").grid(row=1, column=0, padx=10, pady=5)
        self.correo_entry = tk.Entry(root)
        self.correo_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Teléfono:").grid(row=2, column=0, padx=10, pady=5)
        self.telefono_entry = tk.Entry(root)
        self.telefono_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5)
        self.contrasena_entry = tk.Entry(root, show="*")
        self.contrasena_entry.grid(row=3, column=1, padx=10, pady=5)

        registrar_btn = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        registrar_btn.grid(row=4, columnspan=2, pady=10)

    def center_window(self, window):
        window.update_idletasks()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        contrasena = self.contrasena_entry.get()

        registrado, mensaje = registrar_usuario(nombre, correo, telefono, contrasena)
        messagebox.showinfo("Registro de Usuario", mensaje)
        if registrado:
            self.root.destroy()

class InicioSesion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x300")
        self.center_window(self.root)

        tk.Label(root, text="Correo electrónico:").grid(row=0, column=0, padx=10, pady=5)
        self.correo_entry = tk.Entry(root)
        self.correo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.contrasena_entry = tk.Entry(root, show="*")
        self.contrasena_entry.grid(row=1, column=1, padx=10, pady=5)

        iniciar_btn = tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion)
        iniciar_btn.grid(row=2, columnspan=2, pady=10)

    def center_window(self, window):
        window.update_idletasks()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def iniciar_sesion(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()

        iniciado, mensaje = iniciar_sesion(correo, contrasena)
        if iniciado:
            messagebox.showinfo("Inicio de Sesión", mensaje)
            self.root.destroy()

            # Crear una nueva ventana principal
            root = tk.Tk()  # Cambiado de Toplevel a Tk
            Aplicacion(root)
            root.mainloop()
        else:
            messagebox.showerror("Inicio de Sesión", mensaje)

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Ropa al Mayoreo")
        self.root.geometry("300x100")  # Tamaño reducido
        self.position_window()  # Ubicar en la esquina superior izquierda

        self.current_frame = None

        # Crear menú desplegable
        self.crear_menu_desplegable()

    def position_window(self):
        # Posicionar ventana en la esquina superior izquierda
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = 0  # Esquina superior izquierda
        y = 0  # Esquina superior izquierda
        self.root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def crear_menu_desplegable(self):
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

        opciones_combobox = ttk.Combobox(self.root, values=opciones_menu, state="readonly")
        opciones_combobox.pack(side=tk.LEFT, padx=10, pady=10)

        seleccionar_btn = tk.Button(self.root, text="Seleccionar",
                                    command=lambda: self.seleccionar_opcion(opciones_combobox.get()))
        seleccionar_btn.pack(side=tk.LEFT, padx=10, pady=10)

    def seleccionar_opcion(self, opcion):
        # Cerrar ventana anterior si existe
        if self.current_frame is not None:
            self.current_frame.destroy()

        if opcion == "Catalogo":
            self.current_frame = tk.Toplevel(self.root)
            self.current_frame.geometry("900x500")
            CatalogoWindow(self.current_frame)
        elif opcion == "Visualizar usuarios":
            self.current_frame = tk.Toplevel(self.root)
            self.current_frame.geometry("800x400")
            VisualizarUsuariosWindow(self.current_frame)

if __name__ == "__main__":
    root = tk.Tk()
    VentanaBienvenida(root)
    root.mainloop()
