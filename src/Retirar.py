import psycopg2
from decimal import Decimal


class Retirar:
    def retirar(self):
        try:
            conexion = psycopg2.connect(
                host='127.0.0.1',
                port='5432',
                database='test_bd',
                user='postgres',
                password='admin'
            )
            # Crear un cursor
            cursor = conexion.cursor()

            # Solicitar al usuario el monto a retirar
            monto_retiro = Decimal(input("Ingrese el monto a retirar: "))

            # Obtener el saldo actual desde la base de datos
            cursor.execute(
                "SELECT balance FROM usuarios WHERE account = 123456789")
            saldo_actual = cursor.fetchone()[0]

            # Verificar si el saldo es suficiente
            if saldo_actual >= monto_retiro:
                # Actualizar el saldo restando el monto retirado
                saldo_actual -= monto_retiro
                cursor.execute("UPDATE usuarios SET balance = %s WHERE account = 123456789",
                            (saldo_actual,))  # Cambia "tabla_saldo" e "id" según tu estructura de base de datos
                conexion.commit()
                print("Retiro exitoso. Saldo restante:", saldo_actual)
            else:
                print("Saldo insuficiente. Tu saldo es de:", saldo_actual)
        except Exception as e:
                print(f'No ingreses letras, solo numeros')
            # Cerrar la conexión con la base de datos
                cursor.close()
                conexion.close()


if __name__ == '__main__':
    retirar = Retirar()
    retirar.retirar()