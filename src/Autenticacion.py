from base_de_datos.Conexion import Conexion


class Autenticacion:
    def __init__(self, menu):
        self.menu = menu

    def iniciar_sesion(self):
        print("Inicio de sesión")
        nombre = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nombre = %s AND password = %s", (nombre, password))
                count = cursor.fetchone()[0]

                if count > 0:
                    self.menu.usuario_actual = nombre
                    print("Inicio de sesión exitoso.\n")
                else:
                    print("Credenciales incorrectas. Por favor, intente nuevamente.\n")
