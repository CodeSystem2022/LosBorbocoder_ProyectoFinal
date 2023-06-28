from base_de_datos.Conexion import Conexion

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
    else:
        print("Usuario no encontrado")

    cursor.close()
    conexion.commit()
    conexion.close()

if __name__ == '__main__':
    usuario_actual = input("Ingrese el nombre de usuario: ")
    mostrar = MostrarSaldo()
    mostrar.mostrar_saldo(usuario_actual)
