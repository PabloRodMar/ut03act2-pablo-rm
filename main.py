import tablas, insertar, conexion

if __name__ == '__main__':
    # Se iguala a la creación de tablas porque el único lugar en dónde es obligatorio realizar
    # una conexión. Lo explico más a detalle allí.
    db = tablas.crear()
    insertar.insertar_clientes(db)
    insertar.insertar_empleados(db)
    insertar.insertar_proyecto(db)
    while True:
        empleado = input("Introduzca el empleado que trabaja en el proyecto (pulse 0 para salir): ")
        proyecto = input("Introduzca el proyecto en el que el empleado trabajo (pulse 0 para salir): ")
        if empleado == "0" or proyecto == "0":
            break
        insertar.insertar_empleadosproyecto(db, empleado, proyecto)
        