# ventas.py

from modelos import Venta
from datetime import datetime

# Lista de ventas simuladas
ventas_realizadas = [
    Venta(datetime(2024, 7, 15), "Cliente A", ["Camiseta", "Pantalón"], [2, 1], [19.99, 29.99], 69.97),
    Venta(datetime(2024, 7, 14), "Cliente B", ["Zapatos", "Camiseta"], [1, 3], [49.99, 15.99], 112.95),
    Venta(datetime(2024, 7, 13), "Cliente C", ["Pantalón", "Zapatos"], [2, 1], [29.99, 49.99], 109.97)
]

def mostrar_historial_ventas():
    print("\nHistorial de Ventas:")
    for i, venta in enumerate(ventas_realizadas, start=1):
        print(f"\nVenta {i}:")
        print(f"Fecha: {venta.fecha}")
        print(f"Cliente: {venta.cliente}")
        print("Productos vendidos:")
        for producto, cantidad, precio_unitario in zip(venta.productos, venta.cantidades, venta.precios_unitarios):
            print(f"- {producto}: {cantidad} unidades a ${precio_unitario:.2f} cada una")
        print(f"Total de la venta: ${venta.total_venta:.2f}")

# Funciones de filtro y obtención de detalles como se mostró anteriormente
