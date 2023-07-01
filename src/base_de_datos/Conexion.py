from psycopg2 import pool
import psycopg2 as bd
import sys

'''
from src.base_de_datos import Logger
'''
class Conexion:
    _DATABASE = 'usuarios'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtener_conexion(cls):
        try:
            conexion = bd.connect(host=cls._HOST,
                                  user=cls._USERNAME,
                                  password=cls._PASSWORD,
                                  port=cls._DB_PORT,
                                  database=cls._DATABASE)

            #Logger.debug(f'Conexión exitosa: {conexion}')
            return conexion
        except Exception as e:
            #Logger.error(f'Ocurrió un error: {e}')

            sys.exit()

    @classmethod
    def obtener_cursor(cls, conexion):
        return conexion.cursor()

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                      cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)

                #Logger.debug(f'Pool creado con éxito: {cls._pool}')
                return cls._pool
            except Exception as e:
                #Logger.error(f'Hubo un error al obtener el pool de conexión: {e}')

                sys.exit()
        else:
            return cls._pool

if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    conexion2 = Conexion.obtener_conexion()
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
