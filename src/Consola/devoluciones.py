from modelos import Devolucion
from modelos import Producto, Proveedor
from datetime import datetime
from gestion_proveedores import proveedores
from registro_producto import productos_registrados

devoluciones = [
    Devolucion(datetime.now().date(), "Proveedor A", "Producto 1", 5, 100.0),
    Devolucion(datetime.now().date(), "Proveedor B", "Producto 2", 3, 150.0),
    Devolucion(datetime.now().date(), "Proveedor C", "Producto 3", 10, 200.0)
]
def menu_devoluciones():
    print("---Menu Devoluciones---")
    print("1.- Mostrar Devoluciones")
    print("2.- Generar Devolución")
    opcion = input("Elija una Opción: ")
    if opcion == "1":
        mostrar_devoluciones(devoluciones)
    elif opcion == "2":
        genera_devolucion(productos_registrados, proveedores, devoluciones)
    else:
        print("Opción Inválida")
        return

def mostrar_devoluciones(devoluciones):
    for devolucion in devoluciones:
        print(f"Fecha: {devolucion.fecha}\n"
              f"Proveedor: {devolucion.proveedor}\n"
              f"Producto: {devolucion.producto_devuelto}\n"
              f"Cantidad: {devolucion.cantidad}\n"
              f"Costo Recuperado: {devolucion.costo_devolucion}\n")
        print("-" * 40)

def registrar_devolucion(producto, cantidad_devuelta, nombre_proveedor, devoluciones):
    fecha_actual = datetime.now().date()
    costo_recuperado = cantidad_devuelta * producto.preciocosto
    devolucion = Devolucion(fecha_actual, nombre_proveedor, producto.nombre, cantidad_devuelta, costo_recuperado)
    devoluciones.append(devolucion)
    print(f"Devolución registrada: {producto.nombre} - Cantidad devuelta: {cantidad_devuelta}")

def valida_producto(id_producto, productos_registrados):
    for producto in productos_registrados:
        if producto.id_producto == id_producto:
            return producto
    return None

def valida_proveedor(id_proveedor, proveedores):
    for proveedor in proveedores:
        if proveedor.id_proveedor == id_proveedor:
            return proveedor.nombre_empresa
    return None
def validar_opcion_talla():
    while True:
        print("1.- Chica")
        print("2.- Mediana")
        print("3.- Grande")
        talla = input("Seleccione Talla del producto: ")
        if talla in ["1", "2", "3"]:
            return talla
        else:
            print("¡¡Talla Invalida!!")

def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def valida_id_producto():
    while True:
        try:
            id_producto = int(input("ID del Producto: "))
            return id_producto
        except ValueError:
            print("ID de producto inválido. Inténtalo de nuevo.")


def genera_devolucion(productos_registrados, proveedores, devoluciones):
    id_producto = valida_id_producto()
    producto = valida_producto(id_producto, productos_registrados)
    if producto:
        nombre_proveedor = valida_proveedor(producto.id_proveedor, proveedores)
        if nombre_proveedor:
            talla_devuelta = validar_opcion_talla()
            if talla_devuelta == "1":
                cantidad_devuelta = int(input("Ingrese Cantidad a Devolver: "))
                producto.tallachica -= cantidad_devuelta
                registrar_devolucion(producto, cantidad_devuelta, nombre_proveedor, devoluciones)
            elif talla_devuelta == "2":
                cantidad_devuelta = int(input("Ingrese Cantidad a Devolver: "))
                producto.tallamediana -= cantidad_devuelta
                registrar_devolucion(producto, cantidad_devuelta, nombre_proveedor, devoluciones)
            elif talla_devuelta == "3":
                cantidad_devuelta = int(input("Ingrese Cantidad a Devolver: "))
                producto.tallagrande -= cantidad_devuelta
                registrar_devolucion(producto, cantidad_devuelta, nombre_proveedor, devoluciones)
            else:
                print("Talla no válida")
        else:
            print("Proveedor no encontrado")
    else:
        print("Producto no encontrado")