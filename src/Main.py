import logging

from src.models.Usuario import Usuario
from src.models.Transaccion import Transaccion
from src.services.TransaccionService import TransaccionService
from src.services.UsuarioService import UsuarioService
from decimal import *
class Menu:
    def __init__(self):
        self.usuario_actual = None
        self.usuario_service = UsuarioService(self)
        self.transaccion_service = TransaccionService(self)

    def mostrar_menu(self):
        while True:
            if not self.usuario_actual:
                print("***** Bienvenido *****")
                print("1. Registrar usuario")
                print("2. Iniciar sesión")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nombre = input("Ingrese el nombre de usuario: ")
                    password = input("Ingrese la contraseña: ")
                    email = input("Ingrese el correo electrónico: ")
                    user = Usuario(nombre, password, email)
                    self.usuario_service.registrar_usuario(user)
                elif opcion == "2":
                    self.usuario_service.iniciar_sesion()
                elif opcion == "3":
                    break
                else:
                    print("Opción inválida. Por favor, intente nuevamente.\n")
            else:
                self.mostrar_menu_sesion()

    def mostrar_menu_sesion(self):
        while True:
            print("1. Mostrar saldos")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Ver historial")
            print("5. Cerrar sesión")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                if self.usuario_actual:
                    self.transaccion_service.mostrar_saldo(self.usuario_actual)
                else:
                    print("Debe iniciar sesión para ver los saldos.")
            elif opcion == "2" and self.usuario_actual:
                    monto = Decimal(input("Ingrese el monto a depositar: "))
                    transaction = Transaccion(self.usuario_actual, monto, 'Deposito')
                    self.transaccion_service.depositar(transaction)
            elif opcion == "3" and self.usuario_actual:
                    monto = Decimal(input("Ingrese el monto a retirar: "))
                    transaction = Transaccion(self.usuario_actual, monto, 'Retiro')
                    self.transaccion_service.retirar(transaction)
            elif opcion == "4":
                try:
                    self.transaccion_service.mostrarHistorial(self.usuario_actual)
                except Exception as e:
                    print(f'Ha ocurrido un error al intentar acceder a la información: {e}')
                    logging.exception("Aquí le mostramos más información sobre el error: ")
            elif opcion == "5" and self.usuario_actual:
                self.cerrar_sesion()
                print("Gracias por utilizar nuestros servicios")
                break
            elif opcion == "6":
                exit()
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")

    def cerrar_sesion(self):
        if self.usuario_actual:
            self.usuario_actual = None
            print("Se ha cerrado la sesión.")


if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()