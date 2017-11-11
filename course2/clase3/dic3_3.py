'''
Generar una lista de diccionarios con 1000 puntos aleatorios
'''

import random as r


r.seed(a=1980)
lista_dir = []


for i in range(1,21):
    
    lista_dir.append({'x':r.uniform(-10,10),'y':r.uniform(-10,10)})

print(lista_dir)


###filtramos los valores
'''for elem in lista_dir:
    if ( (elem['x']-1)**2+(elem['y']-2)**2 >= 4 ):
        del elem 
'''
'''
lista_2 =[]
for dics in lista_dir:
    if (dics['x']-1)**2 + (dics['y']-2)**2 < 4 :
        lista_2.append(dics)

print("Lista \n")
print(lista_2)

print("Lista \n")
lista3 = []
for dics in lista_dir:
    if dics['x']<0:
        lista3.append(dics)
print(lista3)


lista4=[]
for dics in lista_dir:
    a = dics['x']
    dics['x']=dics['y']
    dics['y']=a
    lista4.append(dics)

print("Lista")
print(lista4)
'''
#########################################################################
#############  Otra   forma     #########################################
############ usando filter   ###########################################
def norm(li):
   return (li['x']-1)**2 + (li['y']-2)**2 < 4


def xneg(li):
    for llave in li.keys():
        if llave =='x':
            return li[llave]<0 
    

dic2 = {'x':-1, 'y':4}
dic1 = {'x': 2,'y':2}
li = [dic1, dic2]



print("Lista \n")
lista3 = filter(xneg,lista_dir)
print(list(lista3))

print("Lista \n")
lista2 = filter(norm,lista_dir)
print(list(lista2))