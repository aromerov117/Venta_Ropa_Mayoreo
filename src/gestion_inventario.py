# gestion_inventario.py

from datetime import datetime
from registro_producto import productos_registrados, editar_producto, buscar_producto_por_id

historial_ajustes_inventario = []

def realizar_ajuste_inventario(usuario, motivo, productos_afectados):
    fecha_hora = datetime.now()
    ajuste = {
        "fecha_hora": fecha_hora,
        "usuario": usuario,
        "motivo": motivo,
        "productos_afectados": productos_afectados
    }
    historial_ajustes_inventario.append(ajuste)

    # Actualizar la cantidad de productos afectados en productos_registrados
    for ajuste_producto in productos_afectados:
        id_producto = ajuste_producto["id"]
        cantidad_afectada = ajuste_producto["cantidad"]
        talla = ajuste_producto.get("talla")

        # Buscar el producto por ID en la lista productos_registrados
        producto = buscar_producto_por_id(id_producto)
        if producto:
            # Realizar el ajuste en la cantidad del producto
            if talla == "chica":
                producto.tallachica += cantidad_afectada
            elif talla == "mediana":
                producto.tallamediana += cantidad_afectada
            elif talla == "grande":
                producto.tallagrande += cantidad_afectada
            else:
                print("Talla no especificada o incorrecta.")
                continue

            # Editar el producto si hay cambios en los datos
            editar_producto(
                id_producto,
                nombre_nuevo=ajuste_producto.get("nuevo_nombre"),
                descripcion_nueva=ajuste_producto.get("nueva_descripcion"),
                tallachica_nueva=ajuste_producto.get("nueva_tallachica"),
                tallamediana_nueva=ajuste_producto.get("nueva_tallamediana"),
                tallagrande_nueva=ajuste_producto.get("nueva_tallagrande"),
                color_nuevo=ajuste_producto.get("nuevo_color"),
                preciocosto_nuevo=ajuste_producto.get("nuevo_preciocosto"),
                precioventa_nuevo=ajuste_producto.get("nuevo_precioventa"),
                id_proveedor_nuevo=ajuste_producto.get("nuevo_id_proveedor")
            )

def mostrar_historial_ajustes():
    if not historial_ajustes_inventario:
        print("No hay ajustes de inventario registrados.")
    else:
        for ajuste in historial_ajustes_inventario:
            print(f"Fecha y hora: {ajuste['fecha_hora']}")
            print(f"Usuario: {ajuste['usuario']}")
            print(f"Motivo: {ajuste['motivo']}")
            print("Productos afectados:")
            for producto in ajuste['productos_afectados']:
                print(f"- ID: {producto['id']}, Cantidad: {producto['cantidad']}, Talla: {producto.get('talla')}")
                if "nuevo_nombre" in producto:
                    print(f"  Nuevo nombre: {producto['nuevo_nombre']}")
                if "nueva_descripcion" in producto:
                    print(f"  Nueva descripción: {producto['nueva_descripcion']}")
                if "nueva_tallachica" in producto:
                    print(f"  Nueva talla chica: {producto['nueva_tallachica']}")
                if "nueva_tallamediana" in producto:
                    print(f"  Nueva talla mediana: {producto['nueva_tallamediana']}")
                if "nueva_tallagrande" in producto:
                    print(f"  Nueva talla grande: {producto['nueva_tallagrande']}")
                if "nuevo_color" in producto:
                    print(f"  Nuevo color: {producto['nuevo_color']}")
                if "nuevo_preciocosto" in producto:
                    print(f"  Nuevo precio costo: {producto['nuevo_preciocosto']}")
                if "nuevo_precioventa" in producto:
                    print(f"  Nuevo precio venta: {producto['nuevo_precioventa']}")
                if "nuevo_id_proveedor" in producto:
                    print(f"  Nuevo ID proveedor: {producto['nuevo_id_proveedor']}")
            print()

def menu_gestion_inventario():
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Realizar ajuste de inventario")
        print("2. Mostrar historial de ajustes de inventario")
        print("3. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Ingresa el nombre del usuario: ")
            motivo = input("Ingresa el motivo del ajuste: ")
            productos_afectados = []
            while True:
                id_producto = input("ID del producto (o 'fin' para terminar): ")
                if id_producto.lower() == 'fin':
                    break
                id_producto = int(id_producto)
                cantidad_afectada = int(input("Cantidad afectada: "))
                talla = input("Talla afectada (chica/mediana/grande): ").lower()
                producto_afectado = {"id": id_producto, "cantidad": cantidad_afectada, "talla": talla}

                # Pedir opcionalmente nuevos datos para el producto
                if input("¿Desea actualizar la información del producto? (s/n): ").lower() == 's':
                    producto_afectado["nuevo_nombre"] = input("Nuevo nombre (o dejar en blanco para no cambiar): ") or None
                    producto_afectado["nueva_descripcion"] = input("Nueva descripción (o dejar en blanco para no cambiar): ") or None
                    producto_afectado["nueva_tallachica"] = int(input("Nueva talla chica (o dejar en blanco para no cambiar): ") or producto_afectado.get("tallachica"))
                    producto_afectado["nueva_tallamediana"] = int(input("Nueva talla mediana (o dejar en blanco para no cambiar): ") or producto_afectado.get("tallamediana"))
                    producto_afectado["nueva_tallagrande"] = int(input("Nueva talla grande (o dejar en blanco para no cambiar): ") or producto_afectado.get("tallagrande"))
                    producto_afectado["nuevo_color"] = input("Nuevo color (o dejar en blanco para no cambiar): ") or None
                    producto_afectado["nuevo_preciocosto"] = float(input("Nuevo precio costo (o dejar en blanco para no cambiar): ") or producto_afectado.get("preciocosto"))
                    producto_afectado["nuevo_precioventa"] = float(input("Nuevo precio venta (o dejar en blanco para no cambiar): ") or producto_afectado.get("precioventa"))
                    producto_afectado["nuevo_id_proveedor"] = int(input("Nuevo ID proveedor (o dejar en blanco para no cambiar): ") or producto_afectado.get("id_proveedor"))

                productos_afectados.append(producto_afectado)
            realizar_ajuste_inventario(usuario, motivo, productos_afectados)
        elif opcion == "2":
            mostrar_historial_ajustes()
        elif opcion == "3":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
