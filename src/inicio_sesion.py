# inicio_sesion.py

from registro import usuarios_registrados
from usuario import Usuario

# Diccionario para rastrear intentos fallidos de inicio de sesión
intentos_fallidos = {}

def iniciar_sesion(correo_electronico, contrasena):
    # Verificar si el correo electrónico está registrado
    for usuario in usuarios_registrados:
        if usuario.correo_electronico == correo_electronico:
            if usuario.contrasena == contrasena:
                # Restablecer intentos fallidos en caso de éxito
                intentos_fallidos[correo_electronico] = 0
                return True, "Inicio de sesión exitoso. Bienvenido al sistema."
            else:
                # Incrementar el contador de intentos fallidos
                if correo_electronico in intentos_fallidos:
                    intentos_fallidos[correo_electronico] += 1
                else:
                    intentos_fallidos[correo_electronico] = 1

                # Verificar si se ha alcanzado el límite de intentos fallidos
                if intentos_fallidos[correo_electronico] >= 3:
                    return False, "Cuenta bloqueada temporalmente por demasiados intentos fallidos."
                return False, "Credenciales incorrectas. Por favor, inténtalo nuevamente."

    return False, "El correo electrónico no está registrado."
