def iniciar_sesion(): #la funcion solicita al usuario su nombre y contraseña
print("Inicio de sesión")
nombre = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

for usuario in usuarios:
if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña: #Verifica si hay coincidencias en la lista usuarios
print("Inicio de sesión exitoso.\n") #Si hay coincidencia muestra el mensaje de inicio de sesion exitoso
return

print("Credenciales incorrectas. Por favor, intente nuevamente.\n") #Si no, el mensaje que intente nuevamente

while True: #se muestra un menú donde el usuario puede seleccionar opciones. Dependiendo de la opcion seleccionada se llama la funcion
print("Bienvenido")
print("1. Registrar usuario")
print("2. Iniciar sesión")
print("3. Salir")
opcion = input("Seleccione una opción: ")

if opcion == "1":
registrar_usuario()
elif opcion == "2":
iniciar_sesion()
elif opcion == "3":
break
else:
print("Opción inválida. Por favor, intente nuevamente.\n")
