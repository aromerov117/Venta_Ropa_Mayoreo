# interfaz_catalogo.py

from registro_producto import productos_registrados

def mostrar_catalogo():
    print("\nCatálogo de Productos:")
    for i, producto in enumerate(productos_registrados, start=1):
        print(f"\nProducto {i}:")
        print(f"Nombre: {producto.nombre}")
        print(f"Descripción: {producto.descripcion}")
        print(f"Talla Chica: {producto.tallachica}")
        print(f"Talla Mediana: {producto.tallamediana}")
        print(f"Talla Grande: {producto.tallagrande}")
        print(f"Color: {producto.color}")
        print(f"Precio Costo: ${producto.preciocosto:.2f}")
        print(f"Precio Venta: ${producto.precioventa:.2f}")
        print(f"ID Proveedor: {producto.id_proveedor}")