# registro_usuario.py

from modelos import Usuario

# Lista de usuarios registrados
usuarios_registrados = [
    Usuario("a", "a", "1234567890", "123", "administrador"),
    Usuario("administrador", "administrador@gmail.com", "1234567890", "123", "administrador"),
    Usuario("gerente", "gerente@gmail.com", "0987654321", "456", "gerente"),
    Usuario("vendedor", "vendedor@gmail.com", "5551234567", "789", "vendedor")
]

# Función para registrar un nuevo usuario
def registrar_usuario(nombre_completo, correo_electronico, telefono, contrasena):
    # Verificar si el correo electrónico ya está registrado
    for usuario in usuarios_registrados:
        if usuario.correo_electronico == correo_electronico:
            return False, "El correo electrónico ya está registrado. Por favor, utiliza otro correo."

    # Si no está registrado, crear un nuevo usuario con el rol "vendedor"
    nuevo_usuario = Usuario(nombre_completo, correo_electronico, telefono, contrasena, "vendedor")
    usuarios_registrados.append(nuevo_usuario)
    return True, "Registro exitoso. Ahora puedes iniciar sesión."

def visualizar_usuarios():
    print("\nLista de Usuarios Registrados:")
    for usuario in usuarios_registrados:
        print(f"Nombre Completo: {usuario.nombre_completo}")
        print(f"Correo Electrónico: {usuario.correo_electronico}")
        print(f"Teléfono: {usuario.telefono}")
        print(f"Rol: {usuario.rol}")
        print("-----------------------------")