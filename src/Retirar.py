from decimal import Decimal
from src.base_de_datos.Conexion import Conexion

class Retirar:
    def retirar(self):
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:

                # Obtener el saldo actual de la base de datos
                cursor.execute('SELECT balance FROM usuarios WHERE "user" = %s',(self.usuario_actual, ))
                saldo_actual = Decimal(cursor.fetchone()[0])
                # Solicitar al usuario el monto a retirar
                monto_retiro = Decimal(input("Ingrese el monto a retirar: "))

                # Verificar si el saldo es suficiente
                if saldo_actual >= monto_retiro:
                    # Actualizar el saldo restando el monto retirado
                    saldo_actual -= monto_retiro
                    cursor.execute('UPDATE usuarios SET "balance" = %s WHERE "user" = %s', (saldo_actual, self.usuario_actual))
                    # Confirmar los cambios en la base de datos
                    conn.commit()
                    print("Retiro exitoso. Saldo actual:", saldo_actual)
                else:
                    print("Saldo insuficiente. Tu saldo es de:", saldo_actual)












if __name__ == '__main__':
    retirar = Retirar()
    retirar.retirar()