'''
La gráfica más sencilla es aquella que grafica puntos X y Y, para lograrlo deberemos proporcionar la lista de valores en X y la lista de valores en Y. Luego mediante la función plot podremos graficar y mostrar la gráfica. Ejecuta el siguiente código y analizalo:

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])

plt.show()
'''

import matplotlib.pyplot as plt

#plt.plot([1,2,3,4,5],[1,4,9,16,25])
#plt.show()


plt.plot([1,2,3,4,5],[1,4,9,16,25], 'g*')
plt.show()


'''
 El método subplots siempre devuelve la figura y una matriz de axis, 
 cada axis nos permitirá dibujar una gráfica independiente:
'''

