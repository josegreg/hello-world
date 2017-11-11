## hacer un csv a partir de una lista de listas de numeros

mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

def T(x):
    return str(x)

###############################################################

f = open("mat2.csv","w")

for row in mat:
    srow = map(T,row)
    linea = ",".join(srow) + '\n'
    f.write(linea)

f.close()
