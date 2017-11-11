## Guardar en un archivo la cadena "hola mundo"
## Crear una función que reciba una lista y la guarde en un archivo
## Crear una función que reciba una lista y obtenga el mínimo, máximo, suma y promedio y los
## guarde en un archivo

file1 = open("texto1.txt","w")
cadena = "hola mundo\n"

for i in cadena:
    file1.write("{}".format(i))

file1.close
