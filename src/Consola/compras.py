# compras.py

from modelos import Compra, Proveedor, Producto

compras_realizadas = [
    Compra("2023-07-01", Proveedor(1, "Proveedor A", "Calle Principal 123", "555-1234", "info@proveedora.com", ["Producto A", "Producto B"]), [("Producto A", 5, 20.0), ("Producto B", 10, 15.0)]),
    Compra("2023-07-05", Proveedor(2, "Proveedor B", "Av. Independencia 456", "555-5678", "info@proveedorb.com", ["Producto C"]), [("Producto C", 7, 25.0)]),
    Compra("2023-07-10", Proveedor(1, "Proveedor A", "Calle Principal 123", "555-1234", "info@proveedora.com", ["Producto A", "Producto B"]), [("Producto A", 3, 20.0), ("Producto D", 8, 30.0)]),
]

def mostrar_historial_compras(compras_realizadas):
    print("\nHistorial de Compras:")
    for i, compra in enumerate(compras_realizadas, start=1):
        print(f"\nCompra {i}:")
        print(f"Fecha: {compra.fecha}")
        print("Productos comprados:")
        for producto, cantidad, precio_unitario in compra.productos_comprados:
            print(f"- {cantidad} x {producto} (${precio_unitario:.2f} c/u)")
        # Verificar el tipo de objeto de compra.proveedor antes de acceder a su nombre
        if isinstance(compra.proveedor, Proveedor):
            print(f"Proveedor: {compra.proveedor.nombre_empresa}")
        else:
            print(f"Proveedor: {compra.proveedor}")  # Imprimir para depurar si es necesario