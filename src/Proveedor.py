class Proveedor:
    def __init__(self, nombre_empresa, direccion, telefono, correo, nombres_productos):
        self.nombre_empresa = nombre_empresa
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.nombres_productos = nombres_productos  # Lista de nombres de productos que vende el proveedor

    def __str__(self):
        productos = ', '.join(self.nombres_productos)
        return (f"Proveedor: {self.nombre_empresa}\nDirección: {self.direccion}\n"
                f"Teléfono: {self.telefono}\nCorreo electrónico: {self.correo}\n"
                f"Productos que vende: {productos}")





