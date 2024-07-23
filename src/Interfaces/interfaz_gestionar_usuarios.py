import tkinter as tk
from tkinter import messagebox
from registro_usuario import usuarios_registrados, buscar_usuario

class GestionarUsuariosWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionar Usuarios")
        self.root.geometry("800x400")
        self.center_window(self.root)

        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.frame, text="Correo electrónico del usuario a editar:").pack(pady=10)
        self.correo_entry = tk.Entry(self.frame)
        self.correo_entry.pack(pady=5)

        editar_btn = tk.Button(self.frame, text="Editar Usuario", command=self.editar_usuario)
        editar_btn.pack(pady=10)

    def center_window(self, window):
        window.update_idletasks()
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def editar_usuario(self):
        correo = self.correo_entry.get()
        usuario = buscar_usuario(correo)

        if usuario:
            nuevo_nombre = tk.simpledialog.askstring("Editar Usuario", "Ingresa el nuevo nombre completo:", initialvalue=usuario.nombre_completo)
            nuevo_correo = tk.simpledialog.askstring("Editar Usuario", "Ingresa el nuevo correo electrónico:", initialvalue=usuario.correo_electronico)
            nuevo_telefono = tk.simpledialog.askstring("Editar Usuario", "Ingresa el nuevo número de teléfono:", initialvalue=usuario.telefono)
            nuevo_rol = tk.simpledialog.askstring("Editar Usuario", "Ingresa el nuevo rol:", initialvalue=usuario.rol)
            nueva_contrasena = tk.simpledialog.askstring("Editar Usuario", "Ingresa la nueva contraseña:", initialvalue=usuario.contrasena)

            if all([nuevo_nombre, nuevo_correo, nuevo_telefono, nuevo_rol, nueva_contrasena]):
                for u in usuarios_registrados:
                    if u.correo_electronico == nuevo_correo and u != usuario:
                        messagebox.showerror("Error", "El correo electrónico ingresado ya está registrado para otro usuario.")
                        return

                confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de editar este usuario?")
                if confirmacion:
                    usuario.nombre_completo = nuevo_nombre
                    usuario.correo_electronico = nuevo_correo
                    usuario.telefono = nuevo_telefono
                    usuario.rol = nuevo_rol
                    usuario.contrasena = nueva_contrasena
                    messagebox.showinfo("Éxito", "Usuario editado exitosamente.")
                else:
                    messagebox.showinfo("Cancelado", "Edición cancelada.")
            else:
                messagebox.showwarning("Advertencia", "Todos los campos deben ser completados.")
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")
