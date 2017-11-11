## Crear una función que reciba una lista y obtenga el mínimo, máximo, suma y promedio y los
## guarde en un archivo

#x debe ser una lista

def resume(L):
    
    f = open("estadistica.txt", "w", encoding='utf-8')
    f.write("La lista es {}\n".format(str(list(L))))
    f.write("Mínimo : {}\n".format(min(L)))
    f.write("Máximo: {}\n".format(max(L)))
    f.write("Suma: {}\n".format(sum(L)))
    f.write("Promedio {}\n".format(sum(L)/len(L)))
    f.write("\n")
    f.close

    return None
####    TERMINA LA FUNCIÓN ###########################



a = range(1,101)

resume(range(1,40,3))