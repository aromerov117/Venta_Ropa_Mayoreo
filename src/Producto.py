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