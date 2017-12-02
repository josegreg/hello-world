import re




pattern = "([\w\.\_\-]+)@([a-zA-Z0-9\.\_\-]+)(\.\w{2,3}){1,2}"

text = "mi correo @es ana@gmail.com y jose@hotmail.com"

text_mod = ""
i=0
for m in re.finditer(pattern,text):
    user = m.group(1)
    print(user)
    if i==0:
        i = m.start(1)
        j = i + len(user)
        text_mod = text[0:i]+"*"*len(user)+text[(j+1):]
        print(text_mod)
    else: 
        text_mod = text_mod[0:i]+"*"*len(user)+text_mod[(j+1):]
    i+=1

print(text_mod)