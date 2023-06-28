#Funcion para registrar a los usuarios
from src.base_de_datos.Conexion import Conexion


def registrar_usuario():
 nombre = input("Ingrese el nombre de usuario: ")
 password = input("Ingrese la contraseña: ")
 email = input("Ingrese el correo electrónico: ")

 with Conexion.obtener_conexion() as conn:
  with conn.cursor() as cursor:
   cursor.execute("SELECT COUNT(*) FROM usuarios WHERE user = %s OR email = %s", (nombre, email))
   count = cursor.fetchone()[0]

   if count > 0:
    print("Error: Ya existe un usuario con ese nombre o correo electrónico.")
   else:
    #se inicializa balance en 0 ya que las columnas son not null y account se auto incrementa
    cursor.execute('INSERT INTO usuarios ("user", password, email, balance) VALUES (%s, %s, %s, 0)', (nombre, password, email))
    conn.commit()
    print("Usuario registrado exitosamente.")

