
def load_matrix_csv(filename):
    f = open(str(filename),"r")
    mat = []

    for line in f:
        srow = line.split(",")
        row = list(map(lambda s: float(s),srow))
        mat.append(row)
    f.close()    
    return mat

def T_CLR_STR(s):
    return s.replace("\n", "").replace(" ", "_")


def load_data_csv(filename):
    
    output = []
    f = open(str(filename),"r")
    
    
    #lin = 0 ## indicador de linea si es 0 es la primera

    line = f.readline()

    columns = line.split(",")
    columns = list(map(lambda s : s.replace("\n","").replace(" ","_"),columns))
    
    
    

    for line in f:
        values = line.split(",")
        values = list(map(T_CLR_STR, values)) # opcional
            
        data = {}
    
        for i in range(0,len(values)):
            key = columns[i]
            value = values[i]
            data[key] = value
        output.append(data)
        
    
    f.close()

    return output
    


def plot_data_pie(data, column):
    import matplotlib.pyplot as plt 
    values  = []

    for dic in data:
        values.append(dic[str(column)])
    print(values)
    pie_dic = {}

    for x in values:
        if x in pie_dic:
            pie_dic[x] +=1
        else:
            pie_dic[x] =1

    labels = []
    size = []
    labels = pie_dic.keys()
    sizes =list(map(lambda s: str(s),pie_dic.values()))
    
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.axis("equal")
    plt.show()
    






def save_matrix_csv(filename,mat):
    f = open(str(filename),"w")
    for row in mat:
        srow = list(map(lambda x: str(x)), row)
        line = ",".join(srow)
        f.write(line+'\n')
    f.close()


def read_line(filename,n):
    f = open(str(filename),"r")
    lineas =f.readlines()
    
    f.close()
    
    return lineas[n-1]


def incluye_col1(data, var,nom1,valor):
    ###data es un diccionario con alguna de sus llaves= var
    d ={}
    for i in data.keys():
        if str(var) == i :
            if float(data[str(var)]) >=valor :
                d[str(nom1)]=  'Si'
            if float(data[str(var)]) < valor :
                d[str(nom1)]=  'No'

    for cla in data.keys():
        d[cla] = data[cla]

    print(d.keys())
    return d



def genera_matrix_csv(filename,num):
    import random  as rnd
    i=0
    rnd.seed(12000)
    f = open(str(filename),"w")
    f.write("Tiempo,Dilatacion,Temperatura,Densidad\n")
    for row in range(0,num):
        row = [ i+1, rnd.randint(0, 10), rnd.uniform(0,100), rnd.uniform(10,50)]
        srow = list(map(lambda x: str(x),row))
        line = ",".join(srow)
        
        f.write(line+'\n')
        i+=1
    f.close()
