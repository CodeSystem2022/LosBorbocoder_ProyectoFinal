from base_de_datos.Conexion import Conexion

#Funcion para registrar a los usuarios
def registrar_usuario():
 nombre = input("Ingrese el nombre de usuario: ")
 password = input("Ingrese la contraseña: ")
 email = input("Ingrese el correo electrónico: ")

 with Conexion.obtener_conexion() as conn:
  with conn.cursor() as cursor:
   cursor.execute("SELECT COUNT(*) FROM usuarios WHERE nombre = %s OR email = %s", (nombre, email))
   count = cursor.fetchone()[0]

   if count > 0:
    print("Error: Ya existe un usuario con ese nombre o correo electrónico.")
   else:
    cursor.execute("INSERT INTO usuarios (nombre, password, email) VALUES (%s, %s, %s)", (nombre, password, email))
    conn.commit()
    print("Usuario registrado exitosamente.")
