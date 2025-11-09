import tablas, insertar, conexion

if __name__ == '__main__':
    db = conexion.conectar_bd()
    tablas.crear()
    insertar.insertar_clientes()