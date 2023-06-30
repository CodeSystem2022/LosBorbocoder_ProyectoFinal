historial_transacciones = []

def agregar_transaccion(transaccion):
    historial_transacciones.append(transaccion)

# Ejemplo de uso
transaccion_1 = {
    'id': 1,
    'fecha': '2023-06-20',
    'descripcion': 'Calzados Flora',
    'monto': 10000.00
}

transaccion_2 = {
    'id': 2,
    'fecha': '2023-06-30',
    'descripcion': 'HBO Max',
    'monto': 972.00
}

transaccion_3 = {
    'id': 3,
    'fecha': '2023-06-15',
    'descripcion': 'Metrogas',
    'monto': 5300.00
}

transaccion_4 = {
    'id': 4,
    'fecha': '2023-06-01',
    'descripcion': 'Recarga de celular',
    'monto': 2500.00
}

transaccion_5 = {
    'id': 5,
    'fecha': '2023-05-30',
    'descripcion': 'Netflix',
    'monto': 4500.00
}

transaccion_6 = {
    'id': 6,
    'fecha': '2023-05-15',
    'descripcion': 'Accesorios Pink',
    'monto': 8000.00
}

agregar_transaccion(transaccion_1)
agregar_transaccion(transaccion_2)
agregar_transaccion(transaccion_3)
agregar_transaccion(transaccion_4)
agregar_transaccion(transaccion_5)
agregar_transaccion(transaccion_6)

# Imprimir historial de transacciones
for transaccion in historial_transacciones:
    print(f"ID: {transaccion['id']}")
    print(f"Fecha: {transaccion['fecha']}")
    print(f"Descripción: {transaccion['descripcion']}")
    print(f"Monto: {transaccion['monto']}")
    print("-------------------")


