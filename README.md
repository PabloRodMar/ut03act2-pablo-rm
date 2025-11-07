# ut04-act2-pablo-rm

Atómico significa que si ocurre un error en la inserción, no se quedan datos sueltos.
Por ejemplo, si uno de los DNI está mal, los anteriores no se añadirán a la tabla de la base de datos.
También se puede usar si, cuando creas un registro, y por ejemplo un campo DATE está mal, el registro no se quede como:
DNI: 12345678P, Nombre: X, Fecha Nacimiento: --, Profesión: --

INSERCIÓN EN BLOQUE DESDE FICHERO USANDO EL MÉTODO bulk_create()
El fichero contiene los datos de los registros en líneas, y en cada línea cada campo
se separa por espacio

Comprobar que el registro no esté en la base de datos:

if not Clientes.select().where(Clientes.dni== nif).exists():
    Clientes.create(dni=nif, nombre=name, nacionalidad=nacion)
else: 
    print ('El cliente ya se encuentra registrado')