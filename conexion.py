from peewee import MySQLDatabase

def conectar_bd():
    try:
        conexion_bd = MySQLDatabase(
            'Empresa',
            user='usuario',
            password='usuario',
            host='127.0.0.1',
            port=3306
        )

        conexion_bd.connect()
        print("Conexión establecida.")
        return conexion_bd

    except Exception as e:
        print("Error: No se pudo conectar con la base de datos: ", e)