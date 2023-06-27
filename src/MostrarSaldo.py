def mostrar_saldo(usuario): #La función muestra el saldo actual del usuario pasado como argumento
 print("Saldo actual: $", usuario["saldo"])

while True:
 print("Bienvenido")
 print("1. Registrar usuario")
 print("2. Iniciar sesión")
 print("3. Mostrar saldo")
 print("4. Salir")

 opcion = input("Seleccione una opción: ")

 if opcion == "1":
  registrar_usuario()
 elif opcion == "2":
  usuario_actual = iniciar_sesion()
 if usuario_actual is None:
  continue
 elif opcion == "3":
  if "usuario_actual" in locals():
   mostrar_saldo(usuario_actual)
  else:
   print("Debe iniciar sesión para ver el saldo.\n")
 elif opcion == "4":
  break
 else:
  print("Opción inválida. Por favor, intente nuevamente.\n")
