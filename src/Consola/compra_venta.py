# compra_venta.py
from datetime import datetime
from compras import *
from ventas import *

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
        id_producto = int(input("ID del producto: "))
        # Buscar el producto por su id_producto
        producto_encontrado = False
        for producto in productos:
            if producto.id_producto == id_producto:
                producto_encontrado = True
                talla = validar_opcion_talla()
                cantidad_nueva = int(input("Cantidad: "))
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
                print(f"Cantidad actualizada: '{producto.nombre}' - Chica: {producto.tallachica}, Mediana: {producto.tallamediana}, Grande: {producto.tallagrande}")
                return

        if not producto_encontrado:
            print("Producto no encontrado.")

    elif opcion == "2":
        id_proveedor = int(input("ID del proveedor: "))
        proveedor_encontrado = False
        # Verificar si el proveedor existe antes de agregar el producto
        for proveedor in proveedores:
            if proveedor.id_proveedor == id_proveedor:
                proveedor_encontrado = True
                nombre_proveedor = proveedor.nombre_empresa
                id_producto = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                descripcion = input("Descripción del producto: ")
                tallachica = int(input("Cantidad de talla chica: "))
                tallamediana = int(input("Cantidad de talla mediana: "))
                tallagrande = int(input("Cantidad de talla grande: "))
                color = input("Color del producto: ")
                precioCosto = float(input("Precio de Costo: "))
                precioVenta = float(input("Precio de Venta: "))
                nuevo_producto = Producto(id_producto, nombre, descripcion, tallachica, tallamediana, tallagrande, color, precioCosto, precioVenta, id_proveedor)
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


#-------------- Ventas ----------------
def mostrar_salida_productos(productos,ventas_realizadas):
    for producto in productos:
        print(producto.mostrarVendedor())

    id_producto = int(input("ID del producto: "))
    lista_productos = []
    lista_cantidades = []
    lista_precios = []
    for producto in productos:
        if producto.id_producto == id_producto:
            print("1.- Chica")
            print("2.- Mediana")
            print("3.- Grande")
            talla = input(f"Seleccione Talla del producto {producto.nombre}: ")

            if talla == "1":
                if producto.tallachica < 1:
                    print("Sin Stock, elige otro producto")
                else:
                    cantidad = int(input("Cantidad: "))
                    nombre_cliente = input("Nombre del Cliente: ")
                    lista_productos.append(producto.nombre)
                    lista_cantidades.append(cantidad)
                    lista_precios.append(producto.precioventa)
                    precioTotal = producto.precioventa * cantidad
                    venta = Venta(datetime.now().date(),nombre_cliente,lista_productos,lista_cantidades,lista_precios,precioTotal,)
                    ventas_realizadas.append(venta)
                    producto.tallachica -= cantidad
                    print("¡¡Venta Realizada!!")

            elif talla == "2":
                if producto.tallamediana < 1:
                    print("Sin Stock, elige otro producto")
                else:
                    cantidad = int(input("Cantidad: "))
                    nombre_cliente = input("Nombre del Cliente")
                    lista_productos.append(producto.nombre)
                    lista_cantidades.append(cantidad)
                    lista_precios.append(producto.precioventa)
                    precioTotal = producto.precioventa * cantidad
                    venta = Venta(datetime.now().date(),nombre_cliente,lista_productos,lista_cantidades,lista_precios,precioTotal,)
                    ventas_realizadas.append(venta)
                    producto.tallachica -= cantidad
                    print("¡¡Venta Realizada!!")

            elif talla == "3":
                if producto.tallagrande < 1:
                    print("Sin Stock, elige otro producto")
                else:
                    cantidad = int(input("Cantidad: "))
                    nombre_cliente = input("Nombre del Cliente")
                    lista_productos.append(producto.nombre)
                    lista_cantidades.append(cantidad)
                    lista_precios.append(producto.precioventa)
                    precioTotal = producto.precioventa * cantidad
                    venta = Venta(datetime.now().date(),nombre_cliente,lista_productos,lista_cantidades,lista_precios,precioTotal,)
                    ventas_realizadas.append(venta)
                    producto.tallachica -= cantidad
                    print("¡¡Venta Realizada!!")

            else:
                print("Opción de talla no válida")

            return

    print("Producto no encontrado")