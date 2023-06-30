from src.base_de_datos.Conexion import Conexion
from src.models.Usuario import Usuario
class UsuarioService:
    def __init__(self, menu):
        self.menu = menu

    def registrar_usuario(self, user: Usuario):
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM usuarios WHERE user = %s OR email = %s",
                               (user.nombre, user.email))
                count = cursor.fetchone()[0]

                if count > 0:
                    print("Error: Ya existe un usuario con ese nombre o correo electrónico.")
                else:
                    cursor.execute('INSERT INTO usuarios ("user", password, email, balance) VALUES (%s, %s, %s, 0)',
                                   (user.nombre, user.password, user.email))
                    conn.commit()
                    print("Usuario registrado exitosamente.")

    def iniciar_sesion(self):
        print("***** Inicio de sesión *****")
        user = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT COUNT(*) FROM usuarios WHERE "user" = %s AND "password" = %s', (user, password))
                cuenta = cursor.fetchone()[0]

                if cuenta > 0:
                    self.menu.usuario_actual = user
                    print("Inicio de sesión exitoso.\n")
                else:
                    print("Credenciales incorrectas. Por favor, intente nuevamente.\n")

