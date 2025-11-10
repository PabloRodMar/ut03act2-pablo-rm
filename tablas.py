from peewee import *
import conexion

base_datos = conexion.conectar_bd()

class BaseModel(Model):
    class Meta:
        database = base_datos


class Cliente(BaseModel):
    dni = CharField(max_length=9, primary_key=True)
    nombre_cliente = CharField()
    tlf = IntegerField()
    email = CharField()

    class Meta:
        table_name = "clientes"


class Empleado(BaseModel):
    dni = CharField(max_length=9, primary_key=True)
    nombre = CharField()
    jefe = BooleanField()
    email = CharField()

    class Meta:
        table_name = "empleados"


class Proyecto(BaseModel):
    titulo_proyecto = CharField()
    descripcion = CharField()
    fecha_inicio = DateField()
    fecha_fin = DateField()
    presupuesto = FloatField()
    fk_cliente = ForeignKeyField(Cliente)
    fk_jefe_proyecto = ForeignKeyField(Empleado)

    class Meta:
        table_name = "proyectos"


class EmpleadosProyecto(BaseModel):
    fk_empleado = ForeignKeyField(Empleado, backref='empleado_proyecto')
    fk_proyecto = ForeignKeyField(Proyecto, backref='empleado_proyecto')

    class Meta:
        table_name = "empleado_proyecto"
        primary_key = CompositeKey('fk_empleado', 'fk_proyecto')


def crear():
    """Crea las tablas si no existen."""
    try:
        base_datos.create_tables([Cliente, Empleado, Proyecto, EmpleadosProyecto])
        print("Tablas creadas correctamente.")
    except Exception as e:
        print("Error: No se pudieron crear las tablas: ", e)
    return base_datos
        