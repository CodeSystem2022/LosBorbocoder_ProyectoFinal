from src.base_de_datos.Conexion import Conexion
from src.models.Transaccion import Transaccion
import locale
from decimal import *

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
                transaccion = Transaccion(self.usuario_actual, monto)
                self.depositar(transaccion)
            elif opcion == '2':
                monto = self.obtener_monto_valido("Ingrese el monto a retirar: ")
                transaccion = Transaccion(self.usuario_actual, monto)
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
            self.actualizar_saldo(transaction.usuario, saldo_actual)
            saldo_formateado = self.formateo_moneda(saldo_actual)
            print(f"¡Depósito exitoso!\n{self.usuario_actual}, su saldo es: {saldo_formateado}.")

    def retirar(self, transaction: Transaccion):
        saldo_actual = self.obtener_saldo(transaction.usuario)
        if saldo_actual is not None:
            if saldo_actual >= transaction.monto:
                saldo_actual -= transaction.monto
                self.actualizar_saldo(transaction.usuario, saldo_actual)
                saldo_formateado = self.formateo_moneda(saldo_actual)
                print(f"¡Retiro exitoso!\n{self.usuario_actual}, su saldo es: {saldo_formateado}.")
            else:
                print("Saldo insuficiente. Tu saldo es de:", saldo_actual)

    def actualizar_saldo(self, user, new_balance):
        with Conexion.obtener_conexion() as conn:
            with conn.cursor() as cursor:
                consulta = 'UPDATE usuarios SET "balance" = %s WHERE "user" = %s'
                cursor.execute(consulta, (new_balance, user))
                conn.commit()

    def formateo_moneda(self, amount):
        return locale.currency(amount)

    def obtener_monto_valido(self, message):
        while True:
            try:
                amount = locale.atof(input(message))
                return Decimal(amount)
            except error:
                print("Monto inválido. Intente nuevamente.")