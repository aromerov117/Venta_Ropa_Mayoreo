# visualizacion_usuarios.py

from registro_usuario import usuarios_registrados

class Usuario:
    def __init__(self, nombre_completo, correo_electronico, telefono, contrasena, rol):
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.contrasena = contrasena
        self.rol = rol

def visualizar_usuarios():
    print("\nLista de Usuarios Registrados:")
    for usuario in usuarios_registrados:
        print(f"Nombre Completo: {usuario.nombre_completo}")
        print(f"Correo Electrónico: {usuario.correo_electronico}")
        print(f"Teléfono: {usuario.telefono}")
        print(f"Rol: {usuario.rol}")
        print("-----------------------------")