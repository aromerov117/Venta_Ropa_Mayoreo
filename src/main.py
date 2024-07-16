from compra_venta import agregar_producto
from Producto import Producto

# Lista para almacenar los productos
productos = []

def agregar_ejemplos():
    producto1 = Producto(1, "Camisa", "Camisa de algodón", "M", "Azul", 20, 15.0, 30.0)
    producto2 = Producto(2, "Pantalón", "Pantalón vaquero", "L", "Negro", 15, 25.0, 50.0)
    productos.append(producto1)
    productos.append(producto2)

def mostrar_inventario():
    print("\nInventario actual:")
    for producto in productos:
        print(producto)
    print()

# Función para vender productos
def vender_producto():
    id_producto = int(input("Ingrese el ID del producto que desea vender: "))
    encontrado = False
    for producto in productos:
        if producto.id_producto == id_producto:
            cantidad = int(input(f"Ingrese la cantidad de '{producto.nombre}' que desea vender: "))
            if cantidad <= producto.cantidad:
                producto.cantidad -= cantidad
                print(f"Venta realizada exitosamente: {cantidad} '{producto.nombre}' vendidos.")
            else:
                print(f"No hay suficiente stock disponible para '{producto.nombre}'.")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

# Función principal (menú)
if __name__ == "__main__":


#--------------------------------Compra Venta-----------------------------------
    agregar_ejemplos()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto(productos)
        elif opcion == '2':
            vender_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-4).")
#------------------------------------------------------------------------------------------------------

