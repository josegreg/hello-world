'''

    Crea una función llamada Integral(f, a, b, n) que reciba los parámetros 
    f - función, 
    a - número, 
    b - número  
    n - número.

    Dentro de la función Integral calcula la integral aproximada con los parámetros enviados y 
    devuelve el dicho valor.

    Ejecuta el siguiente código poniendo antes la definición de la función Integral y corrobora
    que el resultado sea correcto:

'''
import math as mh

# Definimos la función `f` que recibe a `x` y devuelve `x ** 2 - 2 * x + 4`
def f1(x):
    return x ** 2 -2*x +4 

# Definimos las variables para el intervalor de `a` a `b`
a = 0
b = 3

# Definimos el número de particiones, que equivale al número de
# trapecios a formar.




##Crea una funcion llamada integral que reciba los parámetros 

def Integral(funi,a,b,n):


# Creamos un acumulador para almacenar la suma de las áreas que
# equivale a la integral aproximada
    I = 0
    # Calculamos `Δ`
    d = (b - a) / n

# Recorremos 0 <= i < n
    for i in range(0, n):
        # Calculamos xi y xi+1
        xi = a + i * d
        xii = a + (i + 1) * d

    # Obtenemos f(xi) y f(xi+1)
        fi = funi(xi)
        fii = funi(xii)

    # Calculamos Hi
        h = (fi + fii) / 2

    # Sabiendo que todas las bases son iguales a Δ calculamos Ai
        A = d * h

    # Acumulamos el área en la integral aproximada
        I += A
    return I
############ TERMINA FUNCIÓN ##############################################




## Dentro de la funcion Integral calcula la integral aproximada con los parametros enviados y 
## devuelve el dicho valor

integ = Integral(f1,a,b,500)
print("Integral de f(x)={:.4f}".format(integ))


##  Ejecuta el siguiente código poniendo antes la definición de la función Integral y corrobora
##  que el resultado sea correcto:

b=mh.pi/2

## lambda define una función en una misma línea/anónima
## x es el argumento de la función anónima
## después de : viene la definición de la función
## puede ser argumento de otra función

integ2 = Integral(lambda x : mh.cos(x),0,b,50)
print("Integral de f_2(x)={:.4f}".format(integ2))
