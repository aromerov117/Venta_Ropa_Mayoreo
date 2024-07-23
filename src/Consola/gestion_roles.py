# gestion_roles.py

from registro_usuario import usuarios_registrados

def visualizar_roles_y_usuarios(usuarios_registrados):
    roles = {}

    for usuario in usuarios_registrados:
        if usuario.rol not in roles:
            roles[usuario.rol] = []
        roles[usuario.rol].append(usuario)

    while True:
        print("\nRoles disponibles:")
        for i, rol in enumerate(roles, start=1):
            print(f"{i}. {rol.capitalize()} ({len(roles[rol])} usuarios)")

        opcion = input("Selecciona un rol para ver los usuarios (o 'q' para salir): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(roles):
                rol_seleccionado = list(roles.keys())[opcion - 1]
                mostrar_usuarios_por_rol(roles[rol_seleccionado])
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        elif opcion.lower() == 'q':
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_usuarios_por_rol(usuarios):
    while True:
        print(f"\nUsuarios en el rol {usuarios[0].rol.capitalize()}:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario.nombre_completo} - {usuario.correo_electronico} - {usuario.telefono}")

        opcion = input("Presiona 'q' para volver: ")

        if opcion.lower() == 'q':
            break
