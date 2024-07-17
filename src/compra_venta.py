from Producto import Producto

def mostrar_entrada_productos(productos):
    # Mostrar productos existentes
    for producto in productos:
        print(producto)

    id_producto = int(input("ID del producto: "))

    # Buscar el producto por su id_producto
    for producto in productos:
        if producto.id_producto == id_producto:
            print("1.- Chica")
            print("2.- Mediana")
            print("3.- Grande")
            talla = input(f"Seleccione Talla del producto {producto.nombre}: ")
            cantidad_nueva = int(input("Cantidad: "))
            if talla == "1":
                producto.tallachica += cantidad_nueva
            elif talla == "2":
                producto.tallamediana += cantidad_nueva
            elif talla == "3":
                producto.tallagrande += cantidad_nueva
            else:
                print("Talla no válida")
                return
            print(
                f"Cantidad actualizada: '{producto.nombre}' - Chica: {producto.tallachica}, Mediana: {producto.tallamediana}, Grande: {producto.tallagrande}")
            return

    # Si no se encuentra el producto, agregar uno nuevo
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    tallachica = int(input("Cantidad de talla chica: "))
    tallamediana = int(input("Cantidad de talla mediana: "))
    tallagrande = int(input("Cantidad de talla grande: "))
    color = input("Color del producto: ")
    precioCosto = float(input("Precio de Costo: "))
    precioVenta = float(input("Precio de Venta: "))
    id_proveedor = int(input("ID del proveedor: "))

    nuevo_producto = Producto(id_producto, nombre, descripcion, tallachica, tallamediana, tallagrande, color,
                              precioCosto, precioVenta, id_proveedor)
    productos.append(nuevo_producto)

    print("Producto agregado exitosamente!\n")
    print(nuevo_producto)


def mostrar_salida_productos(productos):
    for producto in productos:
        print(producto.mostrarVendedor())

    id_producto = int(input("ID del producto: "))

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
                    producto.tallachica -= cantidad
                    print("¡¡Venta Realizada!!")

            elif talla == "2":
                if producto.tallamediana < 1:
                    print("Sin Stock, elige otro producto")
                else:
                    cantidad = int(input("Cantidad: "))
                    producto.tallamediana -= cantidad
                    print("¡¡Venta Realizada!!")

            elif talla == "3":
                if producto.tallagrande < 1:
                    print("Sin Stock, elige otro producto")
                else:
                    cantidad = int(input("Cantidad: "))
                    producto.tallagrande -= cantidad
                    print("¡¡Venta Realizada!!")

            else:
                print("Opción de talla no válida")

            return

    print("Producto no encontrado")












