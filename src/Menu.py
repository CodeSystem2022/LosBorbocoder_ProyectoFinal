import MostrarSaldo
import RegistrarUsuario
from Autenticacion import Autenticacion
from Depositar import Depositar
from Retirar import Retirar


class Menu:
    def __init__(self):
        self.usuario_actual = None

    def mostrar_menu(self):
        while True:
            print("Bienvenido")
            print("1. Registrar usuario")
            print("2. Iniciar sesión")

            if self.usuario_actual:
                print("3. Mostrar saldos")
                print("4. Depositar")
                print("5. Retirar")

            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                RegistrarUsuario.registrar_usuario()
            elif opcion == "2":
                autenticacion = Autenticacion(self)
                autenticacion.iniciar_sesion()
            elif opcion == "3" and self.usuario_actual:
                MostrarSaldo.mostrar_saldo()
            elif opcion == "4" and self.usuario_actual:
                Depositar.depositar()
            elif opcion == "5" and self.usuario_actual:
                Retirar.retirar()
            elif opcion == "6":
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()
