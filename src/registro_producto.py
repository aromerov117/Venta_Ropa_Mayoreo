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

# Función para buscar un producto por ID
def buscar_producto_por_id(id_producto):
    for producto in productos_registrados:
        if producto.id_producto == id_producto:
            return producto
    return None

# Función para registrar un nuevo producto
def registrar_producto(id_producto, nombre, descripcion, tallachica, tallamediana, tallagrande, color, preciocosto, precioventa, id_proveedor):
    nuevo_producto = Producto(id_producto, nombre, descripcion, tallachica, tallamediana, tallagrande, color, preciocosto, precioventa, id_proveedor)
    productos_registrados.append(nuevo_producto)
    return True, "Producto registrado exitosamente."

# Función para editar un producto existente
def editar_producto(id_producto, nombre_nuevo=None, descripcion_nueva=None, tallachica_nueva=None, tallamediana_nueva=None, tallagrande_nueva=None, color_nuevo=None, preciocosto_nuevo=None, precioventa_nuevo=None, id_proveedor_nuevo=None):
    producto = buscar_producto_por_id(id_producto)
    if producto:
        if nombre_nuevo:
            producto.nombre = nombre_nuevo
        if descripcion_nueva:
            producto.descripcion = descripcion_nueva
        if tallachica_nueva is not None:
            producto.tallachica = tallachica_nueva
        if tallamediana_nueva is not None:
            producto.tallamediana = tallamediana_nueva
        if tallagrande_nueva is not None:
            producto.tallagrande = tallagrande_nueva
        if color_nuevo:
            producto.color = color_nuevo
        if preciocosto_nuevo is not None:
            producto.preciocosto = preciocosto_nuevo
        if precioventa_nuevo is not None:
            producto.precioventa = precioventa_nuevo
        if id_proveedor_nuevo is not None:
            producto.id_proveedor = id_proveedor_nuevo
        return True, "Producto editado exitosamente."
    return False, "Producto no encontrado."
