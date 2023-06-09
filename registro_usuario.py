#Almacenar datos de los usuarios
usuarios = []

#Funcion para registrar a los usuarios
def registrar_usuario():
 print("Registro de usuario")
 nombre = input("Ingrese su nombre: ")
 correo = input("Ingrese su correo electrónico: ")
 contraseña = input("Ingrese su contraseña: ")
 usuario = {
 "nombre": nombre,
 "correo": correo,
 "contraseña": contraseña
 }

 #agrega el usuario al final de la lista
 usuarios.append(usuario)

 print("Usuario registrado exitosamente.\n")