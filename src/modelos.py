# modelos.py

class Usuario:
    def __init__(self, nombre_completo, correo_electronico, telefono, contrasena):
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.contrasena = contrasena

class Producto:
    def __init__(self, nombre, descripcion, precio, disponibilidad, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.disponibilidad = disponibilidad
        self.categoria = categoria

class Venta:
    def __init__(self, fecha, cliente, productos, cantidades, precios_unitarios, total_venta):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos
        self.cantidades = cantidades
        self.precios_unitarios = precios_unitarios
        self.total_venta = total_venta
