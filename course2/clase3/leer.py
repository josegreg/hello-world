'''
leer un archivo csv
'''

def T(s):
    return int(s)

#################################################
f = open("C:/Users/user/Documents/phy/python-cic/clase3/fibo.csv","r")

mat = []

for linea in f:
    srow = linea.split(",")
    row = map(T,list(srow))
    mat.append(list(row))
print(mat) 

f.close()
