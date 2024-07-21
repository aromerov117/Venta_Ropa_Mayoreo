# compras.py

from modelos import Compra, Proveedor, Producto
from gestion_proveedores import proveedores
from datetime import datetime
import csv
'''
compras_realizadas = [
    Compra("2023-07-01", Proveedor(1, "Proveedor A", "Calle Principal 123", "555-1234", "info@proveedora.com", ["Producto A", "Producto B"]), [("Producto A", 5, 20.0), ("Producto B", 10, 15.0)]),
    Compra("2023-07-05", Proveedor(2, "Proveedor B", "Av. Independencia 456", "555-5678", "info@proveedorb.com", ["Producto C"]), [("Producto C", 7, 25.0)]),
    Compra("2023-07-10", Proveedor(1, "Proveedor A", "Calle Principal 123", "555-1234", "info@proveedora.com", ["Producto A", "Producto B"]), [("Producto A", 3, 20.0), ("Producto D", 8, 30.0)]),
]
'''
def cargar_compras_desde_csv(archivo_csv, proveedores_registrados):
    compras_realizadas = []
    try:
        with open(archivo_csv, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convertir la fecha
                fecha = datetime.strptime(row['fecha'], '%Y-%m-%d')

                # Buscar proveedor por ID
                proveedor = next((p for p in proveedores_registrados if p.id_proveedor == int(row['proveedor_id'])),
                                 None)

                if proveedor is None:
                    print(f"Proveedor con ID {row['proveedor_id']} no encontrado.")
                    continue

                # Convertir productos, cantidades y precios en listas
                productos = row['productos'].split(';')
                cantidades = list(map(int, row['cantidades'].split(';')))
                precios = list(map(float, row['precios'].split(';')))

                # Crear lista de tuplas (producto, cantidad, precio)
                productos_comprados = list(zip(productos, cantidades, precios))

                compra = Compra(fecha, proveedor, productos_comprados)
                compras_realizadas.append(compra)
    except FileNotFoundError:
        print(f"El archivo '{archivo_csv}' no se encontró.")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
    return compras_realizadas

archivo_csv = '..\\ArchivosCSV\\compras.csv'
compras_realizadas = cargar_compras_desde_csv(archivo_csv, proveedores)

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