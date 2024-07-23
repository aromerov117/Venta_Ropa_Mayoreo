import tkinter as tk
from tkinter import messagebox
from registro_usuario import usuarios_registrados

class VisualizarUsuariosWindow(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Visualizar Usuarios")
        self.geometry("600x400")
        self.center_window()

        self.mostrar_usuarios()

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def mostrar_usuarios(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Lista de Usuarios Registrados:", font=("Helvetica", 14)).pack(pady=10)

        for usuario in usuarios_registrados:
            tk.Label(self, text=f"Nombre Completo: {usuario.nombre_completo}").pack()
            tk.Label(self, text=f"Correo Electrónico: {usuario.correo_electronico}").pack()
            tk.Label(self, text=f"Teléfono: {usuario.telefono}").pack()
            tk.Label(self, text=f"Contraseña: {usuario.contrasena}").pack()  # Mostrar contraseña para depuración
            tk.Label(self, text=f"Rol: {usuario.rol}").pack()
            tk.Label(self, text="-----------------------------").pack()
