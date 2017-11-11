#### Crear una función que reciba una lista y la guarde en un archivo

##Definimos la funcion

def guarda(lis):
    f=open("texto2.txt","w")
    for el in lis:
        f.write("{}".format(el))
    f.close


x = [1, 2, 3, 4, 5]

guarda(x)

guarda(range(1,21))