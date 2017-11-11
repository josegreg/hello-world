####    PRACTICA ####################
## Para A = [1,5,9,28,32,48,54,99,101]
## 1.- Generar la lista [(impar) ->1,(par)->-1]
## 2.- Generar la siguiente lista - parte entera de numero/10
## 3.- Generar "1/1" "5/5" "9/9" "28/28"


A = [1,5,9,28,32,48,54,99,101]

def imp(a):
    if a%2 ==0:
        return -1
    else:
        return 1


def parte(x):
    return int(x/10)


def imprime_r(x):
    return "{}/{}".format(x,x)

Y = map(imp,A)
Z = map(parte,A)
XX = map(imprime_r,A) 


print(A)
print(Y)
print(list(Z))
print(list(Y))
print(list(XX))