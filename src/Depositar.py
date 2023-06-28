import psycopg2
from decimal import Decimal
from src.base_de_datos.Conexion import Conexion

class Depositar:
    def depositar(self):
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:

                # Obtener el saldo actual de la base de datos
                cursor.execute("SELECT balance FROM usuarios WHERE user = %s ")
                saldo_actual = Decimal(cursor.fetchone()[0])
                monto_a_depositar = input("Ingrese el monto a depositar: ")

        # Calcular el nuevo saldo sumando el monto depositado
        nuevo_saldo = saldo_actual + monto_a_depositar

        # Actualizar el saldo en la base de datos
        cursor.execute("UPDATE usuarios SET balance = %s WHERE account = %s", (nuevo_saldo,))

        # Confirmar los cambios en la base de datos
        conn.commit()

        print("Depósito exitoso. Saldo actualizado.")

        # Cerrar la conexión
        Conexion.close()

if __name__ == '__main__':
    depositar = Depositar()
    depositar.depositar()