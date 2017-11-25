#Ejemplito
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
import graphviz


'''
X = [[0,0],[1,1]]  /* dataset */
Y = [0,1]           /*target o variable a predecir */
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
'''

'''
col1
1-> roja
2 -> naranja

col2
1/->dulce
2->agridulce
3->amargo

col3 forma
1-> semi
2-> regular
3->irregular
'''

X =[
    [1,1,8,1],
    [2,2,8,2],
    [2,3,10,2],
    [2,1,8,2],
    [1,2,8,2]
]

Y=[
    1,
    2,
    3,
    4
]
clf = DecisionTreeClassifier()
clf.fit(X,Y)
R = clf.predict([[2,1,8,1]])
print(R)


dot_data = tree.export_graphviz(clf,out_file= None)
graph = graphviz.Source(dot_data)
graph.render("fruta")

####################################################################################
####################################################################################
######## redes neuronales ##########################################################
####################################################################################

from sklearn.neural_network import MLPClassifier
