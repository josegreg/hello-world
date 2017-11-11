'''
Crear un diccionario que almacene los valores de un producto (nombre, marca, descripción,etc)
'''

#creamos un diccionario

#### leemos una matriz a partir de  un archivo
f= open("mat.csv","r")


def T(s):
    return int(s)



dic1 = {}
i=0
for linea in f:
    srow = linea.split(',')
    row = list(map(T,list(srow)))
    i+=1
    dic1[i]=row
    
for i in dic1.keys():
    print("linea {} = {}".format(i,dic1[i]))

f.close
