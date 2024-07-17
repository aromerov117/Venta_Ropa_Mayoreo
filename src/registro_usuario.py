# registro_usuario.py

from modelos import Usuario

# Lista de usuarios registrados
usuarios_registrados = [
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

    # Si no está registrado, crear un nuevo usuario
    nuevo_usuario = Usuario(nombre_completo, correo_electronico, telefono, contrasena)
    usuarios_registrados.append(nuevo_usuario)
    return True, "Registro exitoso. Ahora puedes iniciar sesión."