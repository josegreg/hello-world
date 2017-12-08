'''
Nombre José Gregorio Rodríguez Villarreal
Crear un programa que recupere los datos del archivo anterior y los guarde 
en la colección experimentos_recuperados
El archivo experimentos.txt debe estar en la misma carpeta
'''


from pymongo import MongoClient
import re

dic = {}

client = MongoClient()

db = client.midb

f = open("experimentos.txt","r")
pattern1 = "tiempo"
pattern2 = "temperatura"
pattern3 = "densidad"
pattern4 = "volumen"

for line in f:
    match1 = re.search(pattern1,line )
    if match1:
        dic['tiempo'] = re.search(r'([0-9]+)\s(\w+)',line).group(1)
    match2 = re.search(pattern2,line)
    
    if match2:
        dic['temperatura'] = re.search(r'([0-9]+\.[0-9]+)\s(\w+)',line).group(1)
    match3 = re.search(pattern3,line )
    if match3:
        dic['densidad'] = re.search(r'([0-9]+\.[0-9]+)\s(kg*\w+)',line).group(1)
    match4 = re.search(pattern4,line )
    if match4:
        dic['volumen'] = re.search(r'([0-9]+\.[0-9]+)\s(m3)',line).group(1)
    match5 = re.search(r'[\-]+',line)
    if match5:    
        db.experimentos_recuperados.insert_one(
        {
            "tiempo":dic['tiempo'],
            "temperatura":dic['temperatura'],
            "densidad":dic['densidad'],
            "volumen":dic['volumen']
        })
        print(dic)

f.close()

print(db.experimentos_recuperados)
