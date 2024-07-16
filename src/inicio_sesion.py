# inicio_sesion.py

from registro_usuario import usuarios_registrados
from modelos import Usuario

intentos_fallidos = {}

def iniciar_sesion(correo_electronico, contrasena):

    # Verificar si el correo electrónico está registrado
    for usuario in usuarios_registrados:
        if usuario.correo_electronico == correo_electronico:
            print(f"Correo electrónico encontrado: {correo_electronico}")  # Depuración
            if usuario.contrasena == contrasena:
                print("Contraseña correcta")  # Depuración
                # Restablecer intentos fallidos en caso de éxito
                intentos_fallidos[correo_electronico] = 0
                return True, "Inicio de sesión exitoso. Bienvenido al sistema."
            else:
                print(f"Contraseña incorrecta: {contrasena}")  # Depuración
                # Incrementar el contador de intentos fallidos
                if correo_electronico in intentos_fallidos:
                    intentos_fallidos[correo_electronico] += 1
                else:
                    intentos_fallidos[correo_electronico] = 1

                # Verificar si se ha alcanzado el límite de intentos fallidos
                if intentos_fallidos[correo_electronico] >= 3:
                    return False, "Cuenta bloqueada temporalmente por demasiados intentos fallidos."
                return False, "Credenciales incorrectas. Por favor, inténtalo nuevamente."

    print(f"Correo electrónico no encontrado: {correo_electronico}")  # Depuración
    return False, "El correo electrónico no está registrado."
