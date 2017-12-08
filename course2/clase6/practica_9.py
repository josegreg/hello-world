'''
Nombre José Gregorio Rodríguez Villarreal

Definir los campos que debería contener un documento que almacena los datos 
de un experimiento, por ejemplo, tiempo, temperatura, densidad, etc.

Crear una colección llamada experimentos con al menos 200 experimentos 
aleatorios.

Recuperar todos los experimentos y guardarlos en un archivo de texto con la 
siguiente estructura, por ejemplo, si los campos de cada experimento son: 
tiempo, temperatura, densidad, se debería construir el archivo:

Antes de correr mongo

Crear siempre C:\data\db

'''
from pymongo import MongoClient
import random as rnd
import math 

client = MongoClient()

db = client.Experimentos




## Crear una coleccion de experimentos
for i in range(1,200):
    db.mi_exp2.insert_one({
        "tiempo": rnd.randint(1,100),
        "temperatura": round(rnd.random(),4),
        "densidad": round(rnd.uniform(10,100),4),
        "volumen": round(rnd.gauss(10,0.05),4)
    })

print(db.mi_exp2)

cursor = db.mi_exp2.find()

fil = open("experimentos.txt",mode = 'w')

for medida in cursor:
    
   #['_id', 'tiempo', 'densidad', 'temperatura', 'volumen']
    fil.write("tiempo: {} MIN \n ".format(medida['tiempo']) )
    fil.write("densidad: {} kg/m3 \n ".format(medida['densidad']) )
    fil.write("temperatura: {} C\n ".format(medida['temperatura']) )
    fil.write("volumen: {} m3\n ".format(medida['volumen']) )
    fil.write("--------------------------------------------\n")

fil.close()