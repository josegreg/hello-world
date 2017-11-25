import matplotlib.pyplot as plt 

labels  = ('Hombres', 'Mujeres','NA')
sizes   = [34,39,10]
explode = (0,0, 0.1) #only explode third

fig, ax = plt.subplots()

ax.pie(sizes, explode = explode, labels = labels, 
        autopct='%1.1f%%', shadow = False, startangle = 90)
        #autopct formato de porcentaje

ax.axis('equal')
plt.show()