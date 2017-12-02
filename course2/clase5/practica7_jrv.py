
'''


    Crea una matriz de experimentos aleatoria,
     donde se midan al menos 8 características de un experimento, 
     por ejemplo, temperatura, presión, humedad, densidad, etc.

    Separar la matriz en X y Y, donde X son las caracterísitcas observables y Y son resultados experimentales.

    Crear un Clasificador (el que desee) y predecir algunos valores similarares a los de su tabla.



'''
import random as rnd
from sklearn import tree


def genera_matrix_csv(filename,num):
    import random  as rnd
    i=0
    rnd.seed(12000)
    f = open(str(filename),"w")
    f.write("Tiempo,Dilatacion,Temperatura,Densidad,Volumen,Presion,salinidad,F7,F8,Respuesta\n")
    for row in range(0,num):
        row = [ i+1, 
                rnd.randint(0, 10), 
                rnd.uniform(0,100), 
                rnd.uniform(10,50),
                rnd.uniform(10,100),
                rnd.gauss(0,1),
                rnd.gauss(10,1),
                rnd.gauss(10,1),
                rnd.gauss(10,5),
                rnd.randint(0,1)]
        srow = list(map(lambda x: str(x),row))
        line = ",".join(srow)
        
        f.write(line+'\n')
        i+=1
    f.close()


def load_matrix_csv(filename):
    f = open(str(filename),"r")
    mat = []
    i=0
    for line in f:
        if i>0:  
            srow = line.split(",")
            row = list(map(lambda s: round(float(s),3),srow))
            mat.append(row)
        i+=1
    f.close()    
    return mat


genera_matrix_csv("mediciones.txt",100)

Mat_exp = load_matrix_csv("mediciones.txt")
print(Mat_exp)

def extrae_ult(L):
    return L[len(L)-1]



Y = list(map(lambda L : int(L[len(L)-1]), Mat_exp))
#print(list(Y))
X = list(map(lambda L : L[:len(L)-1], Mat_exp))
print(list(X))


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
xp = [5.0, rnd.randint(0, 10), 
           rnd.uniform(0,100), 
           rnd.uniform(10,50),
           rnd.uniform(10,100),
           rnd.gauss(0,1),
           rnd.gauss(10,1),
           rnd.gauss(10,1),
           rnd.gauss(10,5)]
print(clf.predict(xp))