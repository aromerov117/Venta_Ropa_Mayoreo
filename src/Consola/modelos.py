# modelos.py

class Usuario:
    def __init__(self, nombre_completo, correo_electronico, telefono, contrasena, rol):
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.contrasena = contrasena
        self.rol = rol


class Producto:
    def __init__(self, id_producto, nombre, descripcion, tallachica, tallamediana, tallagrande, color, preciocosto, precioventa, id_proveedor):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.tallachica = tallachica
        self.tallamediana = tallamediana
        self.tallagrande = tallagrande
        self.color = color
        self.preciocosto = preciocosto
        self.precioventa = precioventa
        self.id_proveedor = id_proveedor

    def __str__(self):
        return (f"ID:{self.id_producto}\tNombre:{self.nombre}\tDescripción:{self.descripcion}\n"
                f"TallaChica:{self.tallachica}\tTallaMediana:{self.tallamediana}\tTallaGrande:{self.tallagrande}\n"
                f"Color: {self.color}\n"
                f"Precio Costo:${self.preciocosto}\tPrecio Venta:${self.precioventa}\tProveedor:{self.id_proveedor}")

    def mostrarVendedor(self):
        return (f"ID:{self.id_producto}\tNombre:{self.nombre}\tDescripcion:{self.descripcion}\n"
                f"TallaChica:{self.tallachica}\tTallaMediana:{self.tallamediana}\tTallaGrande:{self.tallagrande}\n"
                f"Color:{self.color}\tPrecio:${self.precioventa}\t")

class Proveedor:
    def __init__(self, id_proveedor, nombre_empresa, direccion, telefono, correo, productos):
        self.id_proveedor = id_proveedor
        self.nombre_empresa = nombre_empresa
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.productos = productos  # Lista de nombres de productos que el proveedor ofrece

    def __str__(self):
        return f"ID:{self.id_proveedor}\tNombre:{self.nombre_empresa}\tDireccion:{self.direccion}\tTelefono:{self.telefono}\tCorreo:{self.correo}"


class Venta:
    def __init__(self, fecha, cliente, productos, cantidades, precios_unitarios, total_venta):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos
        self.cantidades = cantidades
        self.precios_unitarios = precios_unitarios
        self.total_venta = total_venta

class Compra:
    def __init__(self, fecha, proveedor, productos_comprados):
        self.fecha = fecha
        self.proveedor = proveedor
        self.productos_comprados = productos_comprados

    def obtener_total_compra(self):
        return sum(cantidad * precio_unitario for _, cantidad, precio_unitario in self.productos_comprados)

class Devolucion:
    def __init__(self, fecha, proveedor, producto_devuelto, cantidad, costo_devolucion):
        self.fecha = fecha
        self.proveedor = proveedor
        self.producto_devuelto = producto_devuelto
        self.cantidad = cantidad
        self.costo_devolucion = costo_devolucion


