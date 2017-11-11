'''

    Crea un programa que genere los primero 20 números definidos por la sucesión 
    f(0) = 0, f(1) = 4, f(2) = 3 y f(n) = 2 * f(n - 2) - f(n - 1) + f(n - 2) para n >= 3

'''
lista = list([])
n=20


f_list = [0, 4, 3]
print("Lista inicial de numeros {}".format(f_list)) 


lista.append(f_list[0])
lista.append(f_list[1])
lista.append(f_list[2])
print(lista)
    
for i in range(3,n+1):
    fi = 2*lista[i-2]-lista[i-1]+lista[i-3]
    lista.append(fi)
    
print(lista)
mult_7 = []
 
for i in lista:
        if i%7==0:
            mult_7.append(i)

print(mult_7)

##Otra forma 
mult_7b = filter(lambda x : x%7==0, lista)
print(list(mult_7b))