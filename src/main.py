# main.py

from registro_usuario import registrar_usuario
from inicio_sesion import iniciar_sesion
from ventas import mostrar_historial_ventas
from compras import mostrar_historial_compras
from contabilidad import mostrar_analisis_contabilidad
from catalogo import mostrar_catalogo
from compra_venta import *
from Producto import Producto
from gestion_proveedores import *
opciones_menu = [
    "Catalogo",
    "Entrada de Productos en Inventario",
    "Salida de Productos del Inventario",
    "Registro de Devoluciones de Productos al Proveedor",
    "Gestión de Proveedores y Contactos",
    "Gestión de Ajustes de Inventario",
    "Historial de Ventas",
    "Historial de Compras",
    "Análisis de Contabilidad de Compras y Ventas"
]
# Ejemplo de uso
productos = [
    Producto(1, "Camiseta", "Camiseta de algodón", 10, 5, 3, "Rojo", 20.0, 50.0, 101),
    Producto(2, "Jeans", "Jeans ajustados", 10, 5, 4, "Azul", 35.0, 75.0, 102),
    Producto(3, "Chaqueta", "Chaqueta de cuero", 12, 8, 9, "Negro", 50.0, 100.0, 103),
    Producto(4, "Zapatos", "Zapatos deportivos", 10, 10, 20, "Blanco", 20.0, 60.0, 104),
    Producto(5, "Gorra", "Gorra de béisbol", 20, 20, 13, "Negro", 30.0, 80.0, 105)
]
proveedores = [
    Proveedor(1, "Proveedor A", "Calle Principal 123", "555-1234", "info@proveedora.com", ["Producto A", "Producto B"]),
    Proveedor(2, "Proveedor B", "Av. Independencia 456", "555-5678", "info@proveedorb.com", ["Producto C"])
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
    if opcion == 1:
        mostrar_catalogo()
    elif opcion == 2:
        mostrar_entrada_productos(productos)
    elif opcion == 3:
        mostrar_salida_productos(productos)
    elif opcion == 5:
        menu_proveedores(proveedores)
    elif opcion == 7:
        mostrar_historial_ventas()
    elif opcion == 8:
        mostrar_historial_compras()
    elif opcion == 9:
        mostrar_analisis_contabilidad()
    else:
        print(f"Seleccionaste: {opciones_menu[opcion - 1]}")
        # Aquí puedes agregar la lógica para redirigir al usuario al módulo correspondiente

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
