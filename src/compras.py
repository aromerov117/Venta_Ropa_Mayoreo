# compras.py

from modelos import Compra, Proveedor

# Historial de compras predefinido para pruebas
compras_realizadas = [
    Compra("2023-07-01", Proveedor("Proveedor A"), [("Producto A", 5, 20.0), ("Producto B", 10, 15.0)]),
    Compra("2023-07-05", Proveedor("Proveedor B"), [("Producto C", 7, 25.0)]),
    Compra("2023-07-10", Proveedor("Proveedor A"), [("Producto A", 3, 20.0), ("Producto D", 8, 30.0)]),
]

def mostrar_historial_compras():
    print("\nHistorial de Compras:")
    for i, compra in enumerate(compras_realizadas, start=1):
        print(f"\nCompra {i}:")
        print(f"Fecha: {compra.fecha}")
        print(f"Proveedor: {compra.proveedor.nombre}")
        print("Productos:")
        for producto, cantidad, precio_unitario in compra.productos:
            print(f"- {producto}: {cantidad} unidades a ${precio_unitario:.2f} c/u")
        print(f"Total de la compra: ${compra.obtener_total_compra():.2f}")