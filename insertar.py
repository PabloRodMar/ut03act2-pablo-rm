import os
from datetime import datetime

import peewee
from peewee import *

from tablas import Cliente

db = MySQLDatabase ("hoteles2", host='localhost', port=3306, user='root', password='maido')
db.connect()

def insertar_clientes ():
   
   with open ("ficheros/clientes.txt") as cl:
        for line in cl.readlines():
            users = [Cliente(dni=line.split()[0], nombre = line.split()[1], nacionalidad = line.split()[2])]
        
        with db.atomic():
            Cliente.bulk_create(users)