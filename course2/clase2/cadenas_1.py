##### "A,b,c" -> ["A","b","c"]
##### "10" -> 10

''' 
separador de textos
leer un archivo csv y extraer datos
'''

f = open("datos.csv", "r")

f.readline()

datos = []
for linea in f:
    r=linea.split(",")
    print(r)

    ##agregamos sólo los datos, sin el salto de línea
    datos.append(r[0:(len(r)-1)])

print(datos)
f.close()

 