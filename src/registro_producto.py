# registro_producto.py

from modelos import Producto

# Lista de productos registrados
productos_registrados = [
    Producto("Camiseta básica", "Camiseta de algodón con cuello redondo.", 15.99, True, "Ropa"),
    Producto("Pantalón vaquero", "Vaquero ajustado con bolsillos traseros.", 29.99, False, "Ropa"),
    Producto("Zapatillas deportivas", "Zapatillas ligeras ideales para correr.", 49.99, True, "Calzado")
]

# Función para registrar un nuevo producto
def registrar_producto(nombre, descripcion, precio, disponibilidad, categoria):
    nuevo_producto = Producto(nombre, descripcion, precio, disponibilidad, categoria)
    productos_registrados.append(nuevo_producto)
    return True, "Producto registrado exitosamente."
