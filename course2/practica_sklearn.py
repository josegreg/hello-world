from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier

data = load_breast_cancer()



Y = data.target
print(Y)
X = data.data
print(data.keys())
print(data.feature_names)

Muestra = data.data[:,1:9]
print(Muestra)

clf = DecisionTreeClassifier()
clf.fit(Muestra,Y)

Xp = [[10, 12.5, 18.8, 2, 29, 12.2, 13.5, 32],
        [2,23,4,60,3,2,12,11]]

Yp = clf.predict(Xp)
print(Yp)