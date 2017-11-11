#Ejemplo para abrir un archivo de texto
#Crear un programa que lea cada linea de un archivo e indiquie cuanto mide cada linea

f = open("file1.txt","r")

for linea in f:
    
    print("Contenido: {}\t {}".format(linea[0:(len(linea)-1)],len(linea[0:(len(linea)-1)])))

f.close