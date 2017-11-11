##Este es un comentario
#Dada una lista calcula su promedio.
'''
Este es un bloque de comentario

'''
a= [1,10,3]
promedio = 0

for elem in a:
   promedio +=  float(elem)/len(a)

#Float transforma el entero a flotante
# github.com/badillosoft/python-scic
print(promedio)
print("El promedio de",a," es: ",promedio)