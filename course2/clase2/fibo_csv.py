## Crear un programa que almacene los primeros numeros de la sucesion de fibonacci

def fibos(n):

    fi2 = 1 # f(i - 2)
    fi1 = 1 # f(i - 1)


    f = [1, 1]

#Si ponemos n+1, la lista tendra n+1 elementos, por que iniciamos en 0

    for i in range(2, n ):
        fi = fi1 + fi2

        f.append(fi)
       
        fi2 = fi1
        fi1 = fi
    return tuple(f)


lista = fibos(20) 

f = open("fibo.csv","w")

for elem in lista:
    f.write("{}, ".format(elem))

#Cerramos el archivo
f.close
