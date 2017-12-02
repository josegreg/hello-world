import re 


pattern = "([\w\.\_\-]+)@([a-zA-Z0-9\.\_\-]+)(\.\w{2,3}){1,2}"

text = "mi correo @es ana@gmail.com y jose@hotmail.com"

## groupdict regresa un diccionario con los mathcs
for m in re.finditer(pattern, text):
    print(m.group(1))
    print(m.group(2))