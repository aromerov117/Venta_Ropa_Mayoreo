# gestion_inventario.py

from datetime import datetime
from registro_producto import productos_registrados, editar_producto

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
        nombre_producto = ajuste_producto["nombre"]
        cantidad_afectada = ajuste_producto["cantidad"]

        # Buscar el producto por nombre en la lista productos_registrados
        for producto in productos_registrados:
            if producto.nombre == nombre_producto:
                # Realizar el ajuste en la cantidad del producto
                producto.cantidad += cantidad_afectada
                break

        # Editar el producto si hay cambios en los datos
        if "nuevo_nombre" in ajuste_producto:
            editar_producto(nombre_producto, ajuste_producto["nuevo_nombre"], ajuste_producto["nueva_descripcion"],
                            ajuste_producto["nuevo_precio"], ajuste_producto["nueva_disponibilidad"],
                            ajuste_producto["nueva_categoria"], ajuste_producto["nueva_cantidad"])

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
                print(f"- Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
                if "nuevo_nombre" in producto:
                    print(f"  Nuevo nombre: {producto['nuevo_nombre']}")
                    print(f"  Nueva descripción: {producto['nueva_descripcion']}")
                    print(f"  Nuevo precio: {producto['nuevo_precio']}")
                    print(f"  Nueva disponibilidad: {producto['nueva_disponibilidad']}")
                    print(f"  Nueva categoría: {producto['nueva_categoria']}")
                    print(f"  Nueva cantidad: {producto['nueva_cantidad']}")
            print()
