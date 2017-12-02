import re

texto = """Nombre: Analisis
        Resultados:
        * PH: 27%
        * TEMPERATURA: 120C
        * DILATACION: 5u 
        """

dic = {}        

pattern = "([\*\s]{1,1})([A-Z]+):\s([0-9\.]+)"
pattern2 = "([\*\s]{1,1})([A-Z]+):(\s+)([0-9\.]+)"

for m in re.finditer(pattern2, texto):
    dic[m.group(2)] = int(m.group(4))

for llave in dic.keys():
    print("{} {}".format(llave,dic[llave]))

print(dic)

    

