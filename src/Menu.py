import MostrarSaldo
import RegistrarUsuario
from Autenticacion import Autenticacion
import Depositar
import Retirar

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
                pass
                # saldo.mostrar_saldo()
            elif opcion == "4" and self.usuario_actual:
                pass
                # dep.depositar()
            elif opcion == "5" and self.usuario_actual:
                pass
                # ret.retirar()
            elif opcion == "6":
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()
