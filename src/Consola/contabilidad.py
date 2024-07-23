# contabilidad.py
from fpdf import FPDF
from ventas import ventas_realizadas
from compras import compras_realizadas
from modelos import Proveedor
import matplotlib.pyplot as plt
def mostrar_reporte_compras():
    print("\nReporte de Compras:")
    for compra in compras_realizadas:
        print(f"Fecha: {compra.fecha}")
        if isinstance(compra.proveedor, Proveedor):
            print(f"Proveedor: {compra.proveedor.nombre_empresa}")
        else:
            print(f"Proveedor: {compra.proveedor}")  # Imprime para depurar si es necesario
        for i, producto in enumerate(compra.productos_comprados):
            nombre_producto, cantidad, precio_unitario = producto
            print(f"Producto {i+1}: {nombre_producto} - Cantidad: {cantidad} - Costo Unitario: ${precio_unitario:.2f}")
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
    print("Seleccione una opción:")
    print("1. Mostrar análisis de contabilidad en consola")
    print("2. Generar reporte de contabilidad en PDF")
    print("3. Generar reporte Gráfico")
    opcion = input("Ingrese su opción (1/2/3): ")

    if opcion == "1":
        print("Análisis de Contabilidad de Compras y Ventas:")
        mostrar_reporte_compras()
        mostrar_reporte_ventas()
        print("\nMargen de Ganancia:")
        margen_ganancia = calcular_margen_ganancia()
        print(f"El margen de ganancia total es: ${margen_ganancia:.2f}")
    elif opcion == "2":
        generar_reporte_pdf()
    elif opcion == "3":
        generar_grafico_ventas_por_fecha(ventas_realizadas)
    else:
        print("Opción inválida. Por favor, seleccione 1,2,3.")

class PDFContabilidad(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, 'Reporte de Contabilidad', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", 'B', 10)
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(3)

    def chapter_body(self, body):
        self.set_font("Arial", '', 8)
        self.multi_cell(0, 5, body)
        self.ln(1)

    def add_report_compras(self):
        self.chapter_title("Reporte de Compras:")
        for compra in compras_realizadas:
            self.chapter_body(f"Fecha: {compra.fecha.strftime('%Y-%m-%d')}")
            proveedor = compra.proveedor.nombre_empresa if isinstance(compra.proveedor, Proveedor) else compra.proveedor
            self.chapter_body(f"Proveedor: {proveedor}")
            for i, producto in enumerate(compra.productos_comprados):
                nombre_producto, cantidad, precio_unitario = producto
                self.chapter_body(f"Producto {i + 1}: {nombre_producto} - Cantidad: {cantidad} - Costo Unitario: ${precio_unitario:.2f}")
            self.chapter_body(f"Total de Compra: ${compra.obtener_total_compra():.2f}")
            self.ln(2)

    def add_report_ventas(self):
        self.chapter_title("Reporte de Ventas:")
        for venta in ventas_realizadas:
            self.chapter_body(f"Fecha: {venta.fecha.strftime('%Y-%m-%d')}")
            self.chapter_body(f"Cliente: {venta.cliente}")
            for i, producto in enumerate(venta.productos):
                self.chapter_body(f"Producto {i + 1}: {producto} - Cantidad: {venta.cantidades[i]} - Precio Unitario: ${venta.precios_unitarios[i]:.2f}")
            self.chapter_body(f"Total de Venta: ${venta.total_venta:.2f}")
            self.ln(2)

    def add_analisis_contabilidad(self):
        total_ventas = sum(venta.total_venta for venta in ventas_realizadas)
        total_compras = sum(compra.obtener_total_compra() for compra in compras_realizadas)
        margen_ganancia = total_ventas - total_compras

        self.chapter_title("Análisis de Contabilidad")
        self.chapter_body(f"El margen de ganancia total es: ${margen_ganancia:.2f}")
        self.ln(2)

def generar_reporte_pdf():
    pdf = PDFContabilidad()
    pdf.add_page()

    pdf.add_report_compras()
    pdf.add_report_ventas()
    pdf.add_analisis_contabilidad()

    pdf_output = '..\\Reportes\\reporte_contabilidad.pdf'
    pdf.output(pdf_output)
    print(f"Reporte PDF generado: {pdf_output}")

def generar_grafico_ventas_por_fecha(ventas):
    # Agrupar ventas por fecha
    ventas_por_fecha = {}
    for venta in ventas:
        fecha = venta.fecha.strftime('%Y-%m-%d')  # Convertir la fecha a formato string para el agrupamiento
        if fecha in ventas_por_fecha:
            ventas_por_fecha[fecha] += venta.total_venta
        else:
            ventas_por_fecha[fecha] = venta.total_venta

    # Ordenar fechas
    fechas = sorted(ventas_por_fecha.keys())
    totales = [ventas_por_fecha[fecha] for fecha in fechas]

    # Crear gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(fechas, totales, marker='o', linestyle='-', color='skyblue')
    plt.xlabel('Fecha')
    plt.ylabel('Total de Ventas')
    plt.title('Total de Ventas a lo Largo del Tiempo')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Guardar el gráfico como un archivo en Reportes
    plt.savefig('..\\Reportes\\grafico_ventas_por_fecha.png')
