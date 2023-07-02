from src.base_de_datos.Conexion import Conexion
from src.models.Transaccion import Transaccion
import locale
from decimal import *
from datetime import datetime

class TransaccionService:
    def __init__(self, menu):
        self.menu = menu
        self.usuario_actual = menu.usuario_actual
        locale.setlocale(locale.LC_ALL, '')

    def mostrar_saldo(self, usuario_actual):
        self.usuario_actual = usuario_actual
        saldo = self.obtener_saldo(self.usuario_actual)
        if saldo is not None:
            saldo_formateado = self.formateo_moneda(saldo)
            print(f"{self.usuario_actual}, su saldo es: {saldo_formateado}.")
            print("1- Depositar")
            print("2- Retirar")
            print("3- Volver al menú")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                monto = self.obtener_monto_valido("Ingrese el monto a depositar: ")
                transaccion = Transaccion(self.usuario_actual, monto,  "Deposito")
                self.depositar(transaccion)
            elif opcion == '2':
                monto = self.obtener_monto_valido("Ingrese el monto a retirar: ")
                transaccion = Transaccion(self.usuario_actual, monto, "Retiro")
                self.retirar(transaccion)
            elif opcion == '3':
                pass
                #menu.mostrar_menu_sesion(self)
            else:
                print("Opción incorrecta. Intente nuevamente")
        else:
            print("El usuario no existe.")

    def obtener_saldo(self, usuario_actual):
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                consulta = 'SELECT "balance" FROM usuarios WHERE "user" = %s'
                cursor.execute(consulta, (usuario_actual,))
                resultado = cursor.fetchone()
                return resultado[0] if resultado else None

    def depositar(self, transaction: Transaccion):
        saldo_actual = self.obtener_saldo(transaction.usuario)
        if saldo_actual is not None:
            saldo_actual += transaction.monto
            self.actualizar_saldo(transaction)
            saldo_formateado = self.formateo_moneda(saldo_actual)
            print(f"¡Depósito exitoso!\n{transaction.usuario}, su saldo es: {saldo_formateado}.")

    def retirar(self, transaction: Transaccion):
        saldo_actual = self.obtener_saldo(transaction.usuario)
        if saldo_actual is not None:
            if saldo_actual >= transaction.monto:
                saldo_actual -= transaction.monto
                self.actualizar_saldo(transaction)
                saldo_formateado = self.formateo_moneda(saldo_actual)
                print(f"¡Retiro exitoso!\n{transaction.usuario}, su saldo es: {saldo_formateado}.")
            else:
                print("Saldo insuficiente. Tu saldo es de:", saldo_actual)

    def actualizar_saldo(self, transaction: Transaccion):
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                consulta = 'UPDATE usuarios SET "balance" = %s WHERE "user" = %s'
                cursor.execute(consulta, (transaction.monto, transaction.usuario))
                conn.commit()

                if cursor.rowcount > 0:
                    self.guardar_transaccion(transaction)
                else:
                    print("Error: No se pudo actualizar el saldo.")

    def formateo_moneda(self, amount):
        return locale.currency(amount)

    def obtener_monto_valido(self, message):
        while True:
            try:
                amount = locale.atof(input(message))
                return Decimal(amount)
            except error:
                print("Monto inválido. Intente nuevamente.")

    def guardar_transaccion(self, transaccion: Transaccion):

        """
        Guarda una transacción en la base de datos.
        """
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                try:
                    query = 'INSERT INTO "transactions" ("user", amount, "time", "operation") VALUES (%s, %s, current_timestamp, %s)'
                    cursor.execute(query, (transaccion.usuario, transaccion.monto, transaccion.operacion))
                    conn.commit()
                    print("Transacción guardada exitosamente")
                except psycopg2.Error as e:
                    self.connection.rollback()
                    print(f"Error al guardar la transacción: {e}")

    def obtenerTransacciones(self, usuario):
        """
        Obtiene todas las transacciones de un usuario específico de la base de datos.
        """
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                try:
                    consulta = 'SELECT * FROM "transactions" WHERE "user" = %s'
                    cursor.execute(consulta, (usuario,))
                    transacciones = cursor.fetchall()
                    return transacciones
                except psycopg2.Error as e:
                    print(f"Error al obtener las transacciones: {e}")

    def mostrarHistorial(self, usuario):
        transacciones = self.obtenerTransacciones(usuario)
        if transacciones:
            print("Historial de transacciones:")
            for transaccion in transacciones:

                op = ''

                if (transaccion[4]) == "Deposito":
                    op = 'Deposito: '
                else:
                    op = 'Retiro: '

                date = transaccion[3]
                formatted_date = date.strftime('%d/%m/%Y %H:%M')

                print(f"{op} Fecha: {formatted_date} - Monto: {self.formateo_moneda(transaccion[2])}")
        else:
            print("No se encontraron transacciones para el usuario.")
