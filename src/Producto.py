class Producto:
    def __init__(self, id_producto, nombre, descripcion, talla, color, cantidad, precioCosto, precioVenta):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.talla = talla
        self.color = color
        self.cantidad = cantidad
        self.precioCosto = precioCosto
        self.precioVenta = precioVenta

    def __str__(self):
        return (f"ID: {self.id_producto}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\n"
                f"Talla: {self.talla}\nColor: {self.color}\nCantidad: {self.cantidad}\n"
                f"Precio de costo: ${self.precioCosto}\nPrecio de venta: ${self.precioVenta}")

