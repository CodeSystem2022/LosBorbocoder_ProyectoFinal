from base_de_datos.Conexion import Conexion

class Autenticacion:
    def __init__(self, menu):
        self.menu = menu

    def iniciar_sesion(self):
        print("Inicio de sesión")
        user = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) FROM usuarios WHERE "user" = %s AND "password" = %s', (user, password))
                count = cursor.fetchone()[0]

                if count > 0:
                    self.menu.usuario_actual = user
                    print("Inicio de sesión exitoso.\n")
                else:
                    print("Credenciales incorrectas. Por favor, intente nuevamente.\n")
