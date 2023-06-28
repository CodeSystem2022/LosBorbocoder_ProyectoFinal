import psycopg2
from psycopg2 import connect

class MostrarSaldo:
    def mostrarSaldo(user_id):
        conexion = psycopg2.connect(
            host='127.0.0.1',
            port='5432',
            database='test_bd',
            user='postgres',
            password='admin'
        )

        # Crear un cursor para ejecutar las consultas
        cursor = conexion.cursor()

        # Consulta para obtener el saldo del usuario
        consulta = "SELECT balance FROM usuarios WHERE account = 123456789"
        cursor.execute(consulta)
        

        # Obtener el resultado de la consulta
        resultado = cursor.fetchone()

        if resultado:
            saldo = resultado[0]
            print(f"El saldo del usuario es: {saldo}")
        else:
            print("Usuario no encontrado")

        # Cerrar el cursor y confirmar los cambios en la base de datos
        cursor.close()
        conexion.commit()
        conexion.close()

if __name__ == '__main__':
    mostrar = MostrarSaldo()
    mostrar.mostrarSaldo()
