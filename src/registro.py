# registro.py

from usuario import Usuario

usuarios_registrados = [
    Usuario("Juan Perez", "juan.perez@example.com", "1234567890", "password123"),
    Usuario("Maria Gomez", "maria.gomez@example.com", "0987654321", "securepassword"),
    Usuario("Carlos Ramirez", "carlos.ramirez@example.com", "5551234567", "mysecurepass")
]

def registrar_usuario(nombre_completo, correo_electronico, telefono, contrasena):
    # Verificar si el correo electrónico ya está registrado
    for usuario in usuarios_registrados:
        if usuario.correo_electronico == correo_electronico:
            return False, "El correo electrónico ya está registrado. Por favor, utiliza otro correo."

    # Si no está registrado, crear un nuevo usuario
    nuevo_usuario = Usuario(nombre_completo, correo_electronico, telefono, contrasena)
    usuarios_registrados.append(nuevo_usuario)
    return True, "Registro exitoso. Ahora puedes iniciar sesión."
