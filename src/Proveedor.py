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

