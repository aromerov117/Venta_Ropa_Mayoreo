# main.py

from registro_usuario import registrar_usuario, visualizar_usuarios
from inicio_sesion import iniciar_sesion
from contabilidad import mostrar_analisis_contabilidad
from catalogo import mostrar_catalogo
from compra_venta import *
from gestion_proveedores import *
from edicion_gestion_usuarios import *
from gestion_inventario import menu_gestion_inventario
from registro_producto import productos_registrados

menus = {
    "administrador": [
        "Manejo y administrador de roles",
        "Desbloqueo de cuentas",
        "Recuperacion de respaldos",
        "Visualizar usuarios",
        "Gestionar usuarios"
    ],
    "gerente": [
        "Catalogo",
        "Entrada de Productos en Inventario",
        "Salida de Productos del Inventario",
        "Registro de Devoluciones de Productos al Proveedor",
        "Gestión de Proveedores y Contactos",
        "Gestión de Ajustes de Inventario",
        "Historial de Ventas",
        "Historial de Compras",
        "Análisis de Contabilidad de Compras y Ventas",
        "Visualizar usuarios"
    ],
    "vendedor": [
        "Catalogo",
        "Salida de productos"
    ]
}

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

    iniciado, mensaje, rol = iniciar_sesion(correo_electronico, contrasena)
    if iniciado:
        print(mensaje)
        mostrar_menu(rol)
    else:
        print(mensaje)

def mostrar_menu(rol):
    while True:
        print(f"\nMenú de opciones para {rol}:")
        for i, opcion in enumerate(menus[rol], start=1):
            print(f"{i}. {opcion}")

        opcion = input("Selecciona una opción del menú (o 'q' para salir): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(menus[rol]):
                seleccionar_opcion(opcion, rol)
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        elif opcion.lower() == 'q':
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def seleccionar_opcion(opcion, rol):
    if rol == "administrador":
        if opcion == 1:
            # Implementar la funcionalidad de manejo y administrador de roles
            pass
        elif opcion == 2:
            # Implementar la funcionalidad de desbloqueo de cuentas
            pass
        elif opcion == 3:
            # Implementar la funcionalidad de recuperación de respaldos
            pass
        elif opcion == 4:
            visualizar_usuarios()
        elif opcion == 5:
            editar_usuario()

    elif rol == "gerente":
        if opcion == 1:
            mostrar_catalogo()
        elif opcion == 2:
            mostrar_entrada_productos(productos_registrados, proveedores, compras_realizadas)
        elif opcion == 3:
            mostrar_salida_productos(productos_registrados, ventas_realizadas)
        elif opcion == 4:
            registrar_devolucion_productos(proveedores)
        elif opcion == 5:
            menu_proveedores(proveedores)
        elif opcion == 6:
            menu_gestion_inventario()
        elif opcion == 7:
            mostrar_historial_ventas()
        elif opcion == 8:
            mostrar_historial_compras(compras_realizadas)
        elif opcion == 9:
            mostrar_analisis_contabilidad()
        elif opcion == 10:
            visualizar_usuarios()

    elif rol == "vendedor":
        if opcion == 1:
            mostrar_catalogo()
        elif opcion == 2:
            mostrar_salida_productos(productos_registrados, ventas_realizadas)

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
