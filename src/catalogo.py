# catalogo.py

from modelos import Producto

# Lista de productos simulados
productos_disponibles = [
    Producto("Camiseta básica", "Camiseta de algodón con cuello redondo.", 15.99, True, "Ropa"),
    Producto("Pantalón vaquero", "Vaquero ajustado con bolsillos traseros.", 29.99, False, "Ropa"),
    Producto("Zapatillas deportivas", "Zapatillas ligeras ideales para correr.", 49.99, True, "Calzado")
]

def mostrar_catalogo():
    print("\nCatálogo de Productos:")
    for i, producto in enumerate(productos_disponibles, start=1):
        print(f"\nProducto {i}:")
        print(f"Nombre: {producto.nombre}")
        print(f"Descripción: {producto.descripcion}")
        print(f"Precio: ${producto.precio:.2f}")
        print(f"Disponibilidad: {'Disponible' if producto.disponibilidad else 'No disponible'}")
        print(f"Categoría: {producto.categoria}")