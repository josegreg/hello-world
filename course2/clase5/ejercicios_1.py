'''
Crea un programa que defina la funcion multiplos(m,n) que devuelva una lista con los primeros
n multiplos del numero m comenzando en 1
'''

#definimos la funcion multiplo

def multiplos(m, n):
    mult = [1]

    for i in range(1, n):
        mult.append(m*i)
    
    print("Uno y los multiplos de {} son {}:".format(m, mult))

    return mult


multiplos(7,10)

def multiplos2(m,n):
    
    rango = range(1,n)

    def multi(L):
        if L ==1:
            return 1
        else:
            return L*m

    return list(map(multi,rango))
    
    
print(multiplos2(7,10))
'''
Crea un programa qye defina la funcion criba(m,A)
que ajusta a 0 todos los multiplos de m comenzando en el índice m
'''

#definimos la funcion criba

def criba(m, A):
    
    B = A
    print(B)
    
    for i in range(0, len(B)):
        if B[i]%m == 0 and i >= m-1: ## por que los índices van retrasados por 1
            B[i] = 0
    
    return B


print(criba(5,[1,20,34,45,56,65,75,85,95,10]))


# Programar la criba de Eratóstenes