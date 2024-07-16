# contabilidad.py

from ventas import ventas_realizadas
from compras import compras_realizadas

def mostrar_reporte_compras():
    print("\nReporte de Compras:")
    for compra in compras_realizadas:
        print(f"Fecha: {compra.fecha}")
        print(f"Proveedor: {compra.proveedor.nombre}")
        for i, producto in enumerate(compra.productos):
            print(f"Producto {i+1}: {producto[0]} - Cantidad: {producto[1]} - Costo Unitario: ${producto[2]:.2f}")
        print(f"Total de Compra: ${compra.obtener_total_compra():.2f}")
        print("-" * 30)

def mostrar_reporte_ventas():
    print("\nReporte de Ventas:")
    for venta in ventas_realizadas:
        print(f"Fecha: {venta.fecha}")
        print(f"Cliente: {venta.cliente}")
        for i, producto in enumerate(venta.productos):
            print(f"Producto {i+1}: {producto} - Cantidad: {venta.cantidades[i]} - Precio Unitario: ${venta.precios_unitarios[i]:.2f}")
        print(f"Total de Venta: ${venta.total_venta:.2f}")
        print("-" * 30)

def calcular_margen_ganancia():
    total_ventas = sum(venta.total_venta for venta in ventas_realizadas)
    total_compras = sum(compra.obtener_total_compra() for compra in compras_realizadas)
    margen_ganancia = total_ventas - total_compras
    return margen_ganancia

def mostrar_analisis_contabilidad():
    print("Análisis de Contabilidad de Compras y Ventas:")
    mostrar_reporte_compras()
    mostrar_reporte_ventas()
    print("\nMargen de Ganancia:")
    margen_ganancia = calcular_margen_ganancia()
    print(f"El margen de ganancia total es: ${margen_ganancia:.2f}")

if __name__ == "__main__":
    mostrar_analisis_contabilidad()