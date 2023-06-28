from base_de_datos.Conexion import Conexion
from src import RegistrarUsuario
from src.Autenticacion import Autenticacion


class MostrarSaldo:
    def mostrarSaldo(self, usuario_actual):
        conexion = Conexion.obtener_conexion()

        # Abro cursor
        cursor = conexion.cursor()


        # Consulta para obtener el saldo del usuario
        consulta = ('SELECT balance FROM usuarios WHERE "user" = %s')
        cursor.execute(consulta, (usuario_actual,))


        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        if resultado:
            saldo = resultado[0]
            while True:
                print(f"El saldo del usuario es: {saldo}")
                print("--------------------------")
                print('1 - Volver al menu principal')
                print('2 - Cerrar Sesion')
                valor = input('Seleccione una opcion: ')
                if valor == "2":
                    print('Cerrando sesion...')
                    break
                elif valor == '1':
                        print("3. Mostrar saldos")
                        print("4. Depositar")
                        print("5. Retirar")

                        print("6. Salir")
                        opcion = input("Seleccione una opción: ")

                        if opcion == "1":
                            RegistrarUsuario.registrar_usuario()
                        elif opcion == "2":
                            pass
                            autenticacion = Autenticacion(self)
                            autenticacion.iniciar_sesion()
                        elif opcion == "3" and self.usuario_actual:
                            pass
                            MostrarSaldo.mostrarSaldo(self, self.usuario_actual)
                        elif opcion == "4" and self.usuario_actual:
                            pass
                            # dep.depositar()
                        elif opcion == "5" and self.usuario_actual:
                            pass
                            # ret.retirar()
                        elif opcion == "6":
                            print("Saliendo del programa...")
                            break
                        else:
                            print("Opción inválida. Por favor, intente nuevamente.\n")

                else:
                    print("Opción inválida. Por favor, intente nuevamente.\n")
        else:
            print("Usuario no encontrado")


        cursor.close()
        conexion.commit()
        conexion.close()



if __name__ == '__main__':
    mostrar = MostrarSaldo()
    mostrar.mostrarSaldo(usuario_actual)
