import psycopg2
from decimal import Decimal

class Depositar:

    def depositar(self):
        conexion = psycopg2.connect(
            host='127.0.0.1',
            port='5432',
            database='test_bd',
            user='postgres',
            password='admin'
        )

        # Crear un cursor
        cursor = conexion.cursor()

        # Solicitar el monto a depositar al usuario
        monto = float(input("Ingrese el monto a depositar: "))

        # Obtener el saldo actual de la base de datos
        cursor.execute("SELECT balance FROM usuarios WHERE account = 123456789")
        saldo_actual = Decimal(cursor.fetchone()[0])
        monto_decimal = Decimal(monto)

        # Calcular el nuevo saldo sumando el monto depositado
        nuevo_saldo = saldo_actual + monto_decimal

        # Actualizar el saldo en la base de datos
        cursor.execute("UPDATE usuarios SET balance = %s WHERE account = 123456789", (nuevo_saldo,))

        # Confirmar los cambios en la base de datos
        conexion.commit()

        print("Depósito exitoso. Saldo actualizado.")

        # Cerrar la conexión
        conexion.close()
if __name__ == '__main__':
    depositar = Depositar()
    depositar.depositar()