# interfaz_usuario.py

from registro import registrar_usuario
from inicio_sesion import iniciar_sesion

opciones_menu = [
    "Entrada de Productos en Inventario",
    "Salida de Productos del Inventario",
    "Registro de Devoluciones de Productos al Proveedor",
    "Gestión de Proveedores y Contactos",
    "Gestión de Ajustes de Inventario",
    "Historial de Ventas",
    "Historial de Compras",
    "Análisis de Contabilidad de Compras y Ventas"
]

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
    if iniciado:
        print(mensaje)
        mostrar_menu()
    else:
        print(mensaje)


def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        for i, opcion in enumerate(opciones_menu, start=1):
            print(f"{i}. {opcion}")

        opcion = input("Selecciona una opción del menú (o 'q' para salir): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(opciones_menu):
                seleccionar_opcion(opcion)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        elif opcion.lower() == 'q':
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def seleccionar_opcion(opcion):
    print(f"Seleccionaste: {opciones_menu[opcion - 1]}")
    # Aquí puedes agregar la lógica para redirigir al usuario al módulo correspondiente
    # Por ejemplo, podrías llamar a funciones o clases que manejen cada módulo.


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
