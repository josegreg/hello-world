### Otra forma

fi3 = 3 
fi2 = 4
fi1 = 0


f=[fi1, fi2, fi3]

print("{}\t{}".format(0,f[0]))
print("{}\t{}".format(1,f[1]))
print("{}\t{}".format(2,f[2]))

for i in range(3,21):
    fi = 2*fi2 - fi3 +fi1
    f.append(fi)
    print("{}\t{}".format(i,fi))

    #Actulizamos los valores
    fi2 = fi3
    fi3=fi
    fi1 = fi2
    
