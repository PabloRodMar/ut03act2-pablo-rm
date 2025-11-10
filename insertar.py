import os
from datetime import datetime

from peewee import *

from tablas import Cliente, Empleado, Proyecto, EmpleadosProyecto

def insertar_clientes(db: MySQLDatabase):
    clientes = []
    with open ("ficheros/clientes.txt") as cl:
        for line in cl.readlines():
            dni=line.split()[0]
            nombre_cliente = line.split()[1]
            tlf = line.split()[2]
            email = line.split()[3]
            clientes.append(Cliente(dni=dni, nombre_cliente=nombre_cliente, tlf=tlf, email=email))
        
        with db.atomic():
            Cliente.bulk_create(clientes)

    print("Se han insertado los clientes de manera satisfactoria")


def insertar_empleados(db: MySQLDatabase):
    with db.atomic():
        Empleado.create(dni="23456784X", nombre="Icod", jefe=False, email="icod@empresa.com")
        Empleado.create(dni='99887766E', nombre='Ana Torres', jefe=False, email='ana@empresa.com')
        Empleado.create(dni='87652143J', nombre='Luis Miguel', jefe=True, email='luis@empresa.com')
        Empleado.create(dni='56478381P', nombre='Rocio Aguiar', jefe=True, email='rocio@empresa.com')
        Empleado.create(dni='56756993H', nombre='Amador Rivas', jefe=False, email='amador@empresa.com')

    print("Se han insertado los empleados de manera satisfactoria")


def insertar_proyecto(db: MySQLDatabase):
    proyectos = []
    with open ("ficheros/proyectos.txt") as cl:
        for line in cl.readlines():
            titulo = line.split()[0]
            desc = line.split()[1]
            inicio = line.split()[2]
            fin = line.split()[3]
            budget = line.split()[4]
            cliente = line.split()[5]
            jefe_proyecto = line.split()[6]
            proyectos.append(Proyecto(titulo_proyecto=titulo, descripcion=desc, fecha_inicio=inicio, fecha_fin=fin, presupuesto=budget, fk_cliente=cliente, fk_jefe_proyecto=jefe_proyecto))
        
        with db.atomic():
            Cliente.bulk_create(proyectos)
    
    print("Se han creado los proyectos de manera satisfactoria.")

def insertar_empleadosproyecto(db: MySQLDatabase, empleado, proyecto):
    with db.atomic():
        EmpleadosProyecto.create(fk_empleado=empleado, fk_proyecto=proyecto)