# compras.py
from modelos import Compra, Proveedor
from Proveedor import Proveedor

def mostrar_historial_compras(compra):
    print("\nHistorial de Compras:")
    for i, compra in enumerate(compra, start=1):
        print(f"\nCompra {i}:")
        print(f"Fecha: {compra.fecha}")
        print(f"Proveedor: {compra.proveedor}")
        print("Productos:")
        for producto, cantidad, precio_unitario in compra.productos:
            print(f"- {producto}: {cantidad} unidades a ${precio_unitario:.2f} c/u")
        print(f"Total de la compra: ${compra.obtener_total_compra():.2f}")