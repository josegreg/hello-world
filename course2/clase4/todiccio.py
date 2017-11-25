import scic as sc 


filename = 'archivo.txt'

d = sc.load_data_csv(filename)

#sc.plot_data_pie(d, 'Genero' )

print(d)


d=sc.load
d2 = sc.incluye_col(d, 'Genero')