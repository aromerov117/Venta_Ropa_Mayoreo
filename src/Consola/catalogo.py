# interfaz_catalogo.py
from registro_producto import productos_registrados
from fpdf import FPDF

class PDFCatalogo(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, 'Catálogo de Productos', 0, 1, 'C')
        self.ln(5)

    def product_entry(self, index, producto):
        self.set_font("Arial", 'B', 10)
        self.cell(0, 8, f"Producto {index}:", 0, 1, 'L')

        self.set_font("Arial", '', 8)
        self.multi_cell(0, 5, f"Nombre: {producto.nombre}")
        self.multi_cell(0, 5, f"Descripción: {producto.descripcion}")
        self.multi_cell(0, 5, f"Talla Chica: {producto.tallachica}")
        self.multi_cell(0, 5, f"Talla Mediana: {producto.tallamediana}")
        self.multi_cell(0, 5, f"Talla Grande: {producto.tallagrande}")
        self.multi_cell(0, 5, f"Color: {producto.color}")
        self.multi_cell(0, 5, f"Precio Costo: ${producto.preciocosto:.2f}")
        self.multi_cell(0, 5, f"Precio Venta: ${producto.precioventa:.2f}")
        self.multi_cell(0, 5, f"ID Proveedor: {producto.id_proveedor}")
        self.ln(3)

def mostrar_catalogo():
    while True:
        print("Seleccione una opción:")
        print("1. Mostrar catálogo en consola")
        print("2. Generar catálogo PDF")
        opcion = input("Opción: ")

        if opcion == '1':
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
            break
        elif opcion == '2':
            pdf = PDFCatalogo()
            pdf.add_page()
            for i, producto in enumerate(productos_registrados, start=1):
                pdf.product_entry(i, producto)
            pdf.output('..\\Reportes\\catalogo.pdf')
            print("Catálogo PDF generado con éxito.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

