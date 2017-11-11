'''
Crear un diccionario que almacene los valores de un producto
(nombre, marca, descripcion,costos)
'''

lista_prod = {
    "nombre" : "Fabuloso",
    "marca"  : "Ml",
    "descripcion"   :   "Limpiador de pisos líquido",
    "costos"    :   15,
    "tiendas"   :   ["Gigante","Soriana","Comercial"] 
}
print(lista_prod)

'''
Crear un dicconario que almacene los datos de un experimento
'''

med1 = {
    "nombre" : "Jose",
    "tiempo" : 2.5,
    "PH" : 8,
    "temperatura" : "33.5C"
}

med2 = {
    "nombre" : "Alberto",
    "tiempo" : 1.87,
    "PH" : 4,
    "temperatura" : "34C"
}

med3 = {
    "nombre" : "Oscar",
    "tiempo" : 3.2,
    "PH" : 8,
    "temperatura" : "25C"
}
exp_med = {
    "1" : med1,
    "2" : med2,
    "3" : med3 
}

print(exp_med)