from registro_usuario import usuarios_registrados, Usuario


def mostrar_usuarios():
    print("\nLista de Usuarios Registrados:")
    for usuario in usuarios_registrados:
        print(f"Nombre Completo: {usuario.nombre_completo}")
        print(f"Correo Electrónico: {usuario.correo_electronico}")
        print(f"Teléfono: {usuario.telefono}")
        print(f"Contraseña: {usuario.contrasena}")  # Mostrar contraseña para depuración
        print(f"Rol: {usuario.rol}")
        print("-----------------------------")


def buscar_usuario(correo_electronico):
    for usuario in usuarios_registrados:
        if usuario.correo_electronico == correo_electronico:
            return usuario
    return None


def editar_usuario():
    mostrar_usuarios()
    correo_electronico = input("Ingresa el correo electrónico del usuario que deseas editar: ")
    usuario = buscar_usuario(correo_electronico)

    if usuario:
        print(
            f"\nUsuario encontrado:\nNombre Completo: {usuario.nombre_completo}\nCorreo Electrónico: {usuario.correo_electronico}\nTeléfono: {usuario.telefono}\nRol: {usuario.rol}")

        # Solicitar y validar los nuevos datos del usuario
        nuevo_nombre = input("\nIngresa el nuevo nombre completo del usuario: ")
        nuevo_correo = input("Ingresa el nuevo correo electrónico del usuario: ")
        nuevo_telefono = input("Ingresa el nuevo número de teléfono del usuario: ")
        nuevo_rol = input("Ingresa el nuevo rol del usuario: ")
        nueva_contrasena = input("Ingresa la nueva contraseña del usuario: ")

        # Validar que los campos no estén vacíos
        if (
            nuevo_nombre.strip() == "" or
            nuevo_correo.strip() == "" or
            nuevo_telefono.strip() == "" or
            nuevo_rol.strip() == "" or
            nueva_contrasena.strip() == ""
        ):
            print("\nError: Todos los campos deben ser completados.")
            return

        # Validar que el nuevo correo electrónico no esté registrado para otro usuario
        for u in usuarios_registrados:
            if u.correo_electronico == nuevo_correo and u != usuario:
                print("\nError: El correo electrónico ingresado ya está registrado para otro usuario.")
                return

        # Confirmar la edición
        confirmacion = input("\n¿Estás seguro de editar este usuario? (s/n): ").lower()
        if confirmacion == "s":
            # Realizar la edición
            usuario.nombre_completo = nuevo_nombre
            usuario.correo_electronico = nuevo_correo
            usuario.telefono = nuevo_telefono
            usuario.rol = nuevo_rol
            usuario.contrasena = nueva_contrasena  # Actualizar la contraseña
            print("\nEdición realizada exitosamente.")
        else:
            print("\nEdición cancelada.")
    else:
        print("\nUsuario no encontrado.")
