from Producto import Producto

def agregar_producto(productos):
    id_producto = int(input("ID del producto: "))
    cantidad_nueva = int(input("Cantidad: "))

    # Buscamos el producto por su id_producto
    for producto in productos:
        if producto.id_producto == id_producto:
            producto.cantidad += cantidad_nueva
            print(f"Cantidad actualizada para el producto '{producto.nombre}': {producto.cantidad}")
            return

    # Si no se encontró el producto, se agrega como nuevo
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    talla = input("Talla del producto: ")
    color = input("Color del producto: ")
    precioCosto = float(input("Precio de Costo: "))
    precioVenta = float(input("Precio de Venta: "))

    nuevo_producto = Producto(id_producto, nombre, descripcion, talla, color, cantidad_nueva, precioCosto, precioVenta)
    productos.append(nuevo_producto)

    print("Producto agregado exitosamente!\n")
    print(nuevo_producto)







