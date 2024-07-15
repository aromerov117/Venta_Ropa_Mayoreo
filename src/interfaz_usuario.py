# interfaz_usuario.py

from registro import registrar_usuario
from inicio_sesion import iniciar_sesion


def interfaz_registro():
    print("Bienvenido al registro de usuarios.")
    nombre_completo = input("Ingresa tu nombre completo: ")
    correo_electronico = input("Ingresa tu correo electrónico: ")
    telefono = input("Ingresa tu número de teléfono: ")
    contrasena = input("Ingresa tu contraseña: ")

    registrado, mensaje = registrar_usuario(nombre_completo, correo_electronico, telefono, contrasena)
    print(mensaje)


def interfaz_inicio_sesion():
    print("Bienvenido al inicio de sesión.")
    correo_electronico = input("Ingresa tu correo electrónico: ")
    contrasena = input("Ingresa tu contraseña: ")

    iniciado, mensaje = iniciar_sesion(correo_electronico, contrasena)
    print(mensaje)


if __name__ == "__main__":
    while True:
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            interfaz_registro()
        elif opcion == "2":
            interfaz_inicio_sesion()
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
