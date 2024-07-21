# compra_venta.py
from datetime import datetime
from compras import *
from ventas import *
from datetime import datetime
from modelos import Producto, Proveedor, Compra

def validar_opcion_talla():
    while True:
        print("1.- Chica")
        print("2.- Mediana")
        print("3.- Grande")
        talla = input("Seleccione Talla del producto: ")
        if talla in ["1", "2", "3"]:
            return talla
        else:
            print("Talla inválida, por favor seleccione una opción válida.")


def mostrar_entrada_productos(productos, proveedores, compras):
    # Mostrar productos existentes
    for producto in productos:
        print(producto)

    print("---Menu Compras---")
    print("1 - Comprar Productos en Existencia")
    print("2 - Comprar Producto Nuevo")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        try:
            id_producto = int(input("ID del producto: "))
        except ValueError:
            print("ID del producto debe ser un número entero.")
            return

        # Buscar el producto por su id_producto
        producto_encontrado = False
        for producto in productos:
            if producto.id_producto == id_producto:
                producto_encontrado = True
                talla = validar_opcion_talla()
                if talla is None:
                    return
                try:
                    cantidad_nueva = int(input("Cantidad: "))
                except ValueError:
                    print("Cantidad debe ser un número entero.")
                    return

                if talla == "1":
                    producto.tallachica += cantidad_nueva
                elif talla == "2":
                    producto.tallamediana += cantidad_nueva
                elif talla == "3":
                    producto.tallagrande += cantidad_nueva

                fecha_actual = datetime.now().date()
                id_proveedor = producto.id_proveedor
                nombre_proveedor = ""
                for proveedor in proveedores:
                    if proveedor.id_proveedor == id_proveedor:
                        nombre_proveedor = proveedor.nombre_empresa

                tupla_producto = (producto.nombre, cantidad_nueva, producto.preciocosto)
                lista_tuplas = [tupla_producto]
                nueva_compra = Compra(fecha_actual, nombre_proveedor, lista_tuplas)
                compras.append(nueva_compra)
                print(
                    f"Cantidad actualizada: '{producto.nombre}' - Chica: {producto.tallachica}, Mediana: {producto.tallamediana}, Grande: {producto.tallagrande}")
                return

        if not producto_encontrado:
            print("Producto no encontrado.")
    elif opcion == "2":
        try:
            id_proveedor = int(input("ID del proveedor: "))
        except ValueError:
            print("ID del proveedor debe ser un número entero.")
            return

        proveedor_encontrado = False
        # Verificar si el proveedor existe antes de agregar el producto
        for proveedor in proveedores:
            if proveedor.id_proveedor == id_proveedor:
                proveedor_encontrado = True
                nombre_proveedor = proveedor.nombre_empresa
                try:
                    id_producto = int(input("ID del producto: "))
                    nombre = input("Nombre del producto: ")
                    descripcion = input("Descripción del producto: ")
                    tallachica = int(input("Cantidad de talla chica: "))
                    tallamediana = int(input("Cantidad de talla mediana: "))
                    tallagrande = int(input("Cantidad de talla grande: "))
                    color = input("Color del producto: ")
                    precioCosto = float(input("Precio de Costo: "))
                    precioVenta = float(input("Precio de Venta: "))
                except ValueError:
                    print("Los valores de ID, cantidad tallas, precio de costo y precio de venta deben ser numéricos.")
                    return

                nuevo_producto = Producto(id_producto, nombre, descripcion, tallachica, tallamediana, tallagrande,
                                          color, precioCosto, precioVenta, id_proveedor)
                productos.append(nuevo_producto)

                lista_tuplas = []
                if tallachica > 0:
                    tupla_producto = (nuevo_producto.nombre, tallachica, nuevo_producto.preciocosto)
                    lista_tuplas.append(tupla_producto)
                if tallamediana > 0:
                    tupla_producto = (nuevo_producto.nombre, tallamediana, nuevo_producto.preciocosto)
                    lista_tuplas.append(tupla_producto)
                if tallagrande > 0:
                    tupla_producto = (nuevo_producto.nombre, tallagrande, nuevo_producto.preciocosto)
                    lista_tuplas.append(tupla_producto)

                nueva_compra = Compra(datetime.now().date(), nombre_proveedor, lista_tuplas)
                compras.append(nueva_compra)
                print("Producto agregado exitosamente!\n")
                print(nuevo_producto)
                break

        if not proveedor_encontrado:
            print("El proveedor no existe")
    else:
        print("Opcion invalida")


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


#-------------- Ventas ----------------
def mostrar_salida_productos(productos, ventas_realizadas):
    for producto in productos:
        print(producto.mostrarVendedor())

    try:
        id_producto = int(input("ID del producto: "))
    except ValueError:
        print("ID de producto inválido. Debe ser un número entero.")
        return

    producto_seleccionado = None
    for producto in productos:
        if producto.id_producto == id_producto:
            producto_seleccionado = producto
            break

    if not producto_seleccionado:
        print("Producto no encontrado")
        return

    talla = validar_opcion_talla()

    if talla == "1":
        if producto_seleccionado.tallachica < 1:
            print("Sin Stock, elige otro producto")
            return
        else:
            cantidad = validar_cantidad()
            if cantidad > producto_seleccionado.tallachica:
                print("Cantidad excede el stock disponible. Elige otra cantidad.")
                return
            nombre_cliente = input("Nombre del Cliente: ")
            lista_productos = [producto_seleccionado.nombre]
            lista_cantidades = [cantidad]
            lista_precios = [producto_seleccionado.precioventa]
            precioTotal = producto_seleccionado.precioventa * cantidad
            venta = Venta(datetime.now().date(), nombre_cliente, lista_productos, lista_cantidades, lista_precios, precioTotal)
            ventas_realizadas.append(venta)
            producto_seleccionado.tallachica -= cantidad
            print("¡¡Venta Realizada!!")
    elif talla == "2":
        if producto_seleccionado.tallamediana < 1:
            print("Sin Stock, elige otro producto")
            return
        else:
            cantidad = validar_cantidad()
            if cantidad > producto_seleccionado.tallamediana:
                print("Cantidad excede el stock disponible. Elige otra cantidad.")
                return
            nombre_cliente = input("Nombre del Cliente: ")
            lista_productos = [producto_seleccionado.nombre]
            lista_cantidades = [cantidad]
            lista_precios = [producto_seleccionado.precioventa]
            precioTotal = producto_seleccionado.precioventa * cantidad
            venta = Venta(datetime.now().date(), nombre_cliente, lista_productos, lista_cantidades, lista_precios, precioTotal)
            ventas_realizadas.append(venta)
            producto_seleccionado.tallamediana -= cantidad
            print("¡¡Venta Realizada!!")
    elif talla == "3":
        if producto_seleccionado.tallagrande < 1:
            print("Sin Stock, elige otro producto")
            return
        else:
            cantidad = validar_cantidad()
            if cantidad > producto_seleccionado.tallagrande:
                print("Cantidad excede el stock disponible. Elige otra cantidad.")
                return
            nombre_cliente = input("Nombre del Cliente: ")
            lista_productos = [producto_seleccionado.nombre]
            lista_cantidades = [cantidad]
            lista_precios = [producto_seleccionado.precioventa]
            precioTotal = producto_seleccionado.precioventa * cantidad
            venta = Venta(datetime.now().date(), nombre_cliente, lista_productos, lista_cantidades, lista_precios, precioTotal)
            ventas_realizadas.append(venta)
            producto_seleccionado.tallagrande -= cantidad
            print("¡¡Venta Realizada!!")
    else:
        print("Opción de talla no válida")