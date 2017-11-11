#### leemos una matriz a partir de  un archivo
f= open("c:/Users/user/Documents/phy/python-cic/clase3/mat.csv","r")


def T(s):
    return int(s)



mat = []

for linea in f:
    srow = linea.split(',')
    row = list(map(T,list(srow)))
    mat.append(row)

print(mat)
f.close