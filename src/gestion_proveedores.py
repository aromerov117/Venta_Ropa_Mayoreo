from modelos import Proveedor

def registrar_proveedor(proveedores):
    id_proveedor = int(input("Ingrese el ID del proveedor: "))
    nombre_empresa = input("Ingrese el nombre de la empresa: ")
    direccion = input("Ingrese la dirección: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo electrónico: ")

    productos = []  # Lista para los productos que ofrece el proveedor

    while True:
        nombre_producto = input("Ingrese el nombre del producto que ofrece (deje en blanco para terminar): ")
        if not nombre_producto:
            break
        productos.append(nombre_producto)

    proveedor = Proveedor(id_proveedor, nombre_empresa, direccion, telefono, correo, productos)
    proveedores.append(proveedor)
    print("Proveedor registrado exitosamente!\n")

def mostrar_proveedores(proveedores):
    print("Proveedores registrados:")
    for proveedor in proveedores:
        print(proveedor)
        print("Productos:")
        for producto in proveedor.productos:
            print(f"- {producto}")
        print("\n")


def menu_proveedores(proveedores):
    while True:
        print("\n--- Menú de Proveedores ---")
        print("1. Mostrar proveedores")
        print("2. Registrar proveedor")
        print("3. Eliminar proveedor")
        print("4. Volver al menú principal")

        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                mostrar_proveedores(proveedores)
            elif opcion == 2:
                registrar_proveedor(proveedores)
            elif opcion == 3:
                eliminar_proveedor(proveedores)
            elif opcion == 4:
                print("Volviendo al menú principal...")
                return
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Error: Ingrese un número válido como opción.")
def eliminar_proveedor(proveedores):
    mostrar_proveedores(proveedores)
    id_proveedor = int(input("Ingrese el ID del proveedor a Eliminar: "))
    proveedores.pop(id_proveedor-1)
    print(f"!!Proveedor {id_proveedor} Eliminado!!")




