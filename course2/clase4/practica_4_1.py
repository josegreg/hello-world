import scic as sc 
import matplotlib.pyplot as plt 


num =10
filename = "experimento.txt"
param1 = 60
param2 = 4



sc.genera_matrix_csv(filename, num)


d2 = sc.load_data_csv(filename)

#print(d2)
## d2 es una lista de diccionarios




##Ahora aplicamos la funcion incluye_col1 y  a la lista de diccionarios
d3 = []
for elem in d2:
    d3.append(sc.incluye_col1(elem,'Temperatura','Invalido',param1))
d4 = []
for elem in d3:
    d4.append(sc.incluye_col1(elem,'Dilatacion','Sobredilatado',param2))
print(d4)

#sc.plot_data_pie(d3,'Invalido')
##############################################################

values  = []

for dic in d4:
    values.append(dic['Invalido'])

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
    


for dic in d4:
    values.append(dic['Sobredilatado'])

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
    
