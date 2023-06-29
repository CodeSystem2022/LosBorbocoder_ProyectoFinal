from base_de_datos.Conexion import Conexion
from src.Depositar import Depositar
from src.Menu import Menu
from src.Retirar import Retirar

def mostrar_saldo(self, usuario_actual):
    # Obtener la conexión desde la clase Conexion
    conexion = Conexion.obtener_conexion()

    # Abro cursor

    cursor = conexion.cursor()

    # Consulta para obtener el saldo del usuario

    consulta = 'SELECT balance FROM usuarios WHERE "user" = %s'
    cursor.execute(consulta, (usuario_actual,))

    # Obtener el resultado de la consulta

    resultado = cursor.fetchone()

    if resultado:
        saldo = resultado[0]
        print(f"El saldo del usuario es: {saldo}")
        print("1- Depositar")
        print("2- Retirar")
        print("3- Volver al menu")
        opcion = input ("Seleccione una opcion: ")
        if opcion == '1':
            Depositar.depositar(self)
        elif opcion == '2':
            Retirar.retirar(self)
        elif opcion == '3':
            Menu.mostrar_menu_sesion(self)
        else:
            print("Opcion incorrecta. Intente nuevamente")

    else:
        print("Usuario no encontrado")

    cursor.close()
    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    usuario_actual = input("Ingrese el nombre de usuario: ")
    mostrar = MostrarSaldo()
    mostrar.mostrar_saldo(usuario_actual)

