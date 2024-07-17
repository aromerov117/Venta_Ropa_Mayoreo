# registro_producto.py

from modelos import Producto

# Lista de productos registrados
productos_registrados = [
    Producto(1, "Camiseta", "Camiseta de algodón", 10, 5, 3, "Rojo", 20.0, 50.0, 1),
    Producto(2, "Jeans", "Jeans ajustados", 10, 5, 4, "Azul", 35.0, 75.0, 2),
    Producto(3, "Chaqueta", "Chaqueta de cuero", 12, 8, 9, "Negro", 50.0, 100.0, 1),
    Producto(4, "Zapatos", "Zapatos deportivos", 10, 10, 20, "Blanco", 20.0, 60.0, 2),
    Producto(5, "Gorra", "Gorra de béisbol", 20, 20, 13, "Negro", 30.0, 80.0, 1)
]


# Función para registrar un nuevo producto
def registrar_producto(nombre, descripcion, precio, disponibilidad, categoria, cantidad):
    nuevo_producto = Producto(nombre, descripcion, precio, disponibilidad, categoria, cantidad)
    productos_registrados.append(nuevo_producto)
    return True, "Producto registrado exitosamente."


# Función para editar un producto existente
def editar_producto(nombre_buscar, nombre_nuevo, descripcion_nueva, precio_nuevo, disponibilidad_nueva, categoria_nueva,
                    cantidad_nueva):
    for producto in productos_registrados:
        if producto.nombre == nombre_buscar:
            producto.nombre = nombre_nuevo
            producto.descripcion = descripcion_nueva
            producto.precio = precio_nuevo
            producto.disponibilidad = disponibilidad_nueva
            producto.categoria = categoria_nueva
            producto.cantidad = cantidad_nueva
            return True, "Producto editado exitosamente."

    return False, "Producto no encontrado."
