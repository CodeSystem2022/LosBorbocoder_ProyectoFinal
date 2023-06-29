
import RegistrarUsuario
from Autenticacion import Autenticacion

import Retirar
from src import Depositar, MostrarSaldo
from src.Depositar import Depositar

class Menu:
    def __init__(self):
        self.usuario_actual = None

    def mostrar_menu(self):
        while True:
            if not self.usuario_actual:
                print("Bienvenido")
                print("1. Registrar usuario")
                print("2. Iniciar sesión")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    RegistrarUsuario.registrar_usuario()
                elif opcion == "2":
                    autenticacion = Autenticacion(self)
                    autenticacion.iniciar_sesion()

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
            print("4. Cerrar sesión")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
            
                if self.usuario_actual:
                    MostrarSaldo.mostrar_saldo(self, self.usuario_actual)
                else:
                    print("Debe iniciar sesión para ver los saldos.")
                    
            elif opcion == "2" and self.usuario_actual:
                 Depositar.depositar()
            elif opcion == "3" and self.usuario_actual:
                 Retirar.retirar()
            elif opcion == "4" and self.usuario_actual:
                self.usuario_actual = None
                break
            elif opcion == "5":

                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.\n")

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()
