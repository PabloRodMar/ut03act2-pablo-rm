import os
from datetime import datetime

import peewee
from peewee import *

from tablas import Cliente

import conexion

db = conexion.conectar_bd()

def insertar_clientes ():
   
   with open ("ficheros/clientes.txt") as cl:
        for line in cl.readlines():
            dni=line.split()[0]
            nombre_cliente = line.split()[1]
            tlf = line.split()[2]
            email = line.split()[3]
            users = [Cliente(dni=dni, nombre_cliente=nombre_cliente, tlf=tlf, email=email)]
        
        with db.atomic():
            Cliente.bulk_create(users)