string = "{[()[]"
pilha = []
correto = True
for i in string:
    
    if i== "(" or i=="[" or i=="{":
        pilha.append(i)
        topo = i
    else:
        if pilha != []:
            if (i == ")" and topo == "(" ) or (i=="]" and topo=="[") or (i=="}" and topo=="{"):    
                if len(pilha) > 0:
                    pilha.pop()
                    if len(pilha) > 0:
                        topo = pilha[len(pilha)-1]
            else:
                correto = False
        else:
            correto = False

if (len(pilha) == 0) and (correto == True):
    print("casada")
else:
    print("nao casada")

lista = []
for i in string:
    lista.append(i)
print(lista)

d = [('(', "1"), (')', "1"),('[', "2"), (']', "2"), ('{', "3"), ('}', "3")]
dicio = dict(d)

s = ''
for i in lista:
    s += dicio[i]

print(s)

# Will Tentativa
for i in range(len(s)):
    if(s[i] == "1"):
        if(s[i] != [0]):
            if(s[i-1] == "2" or s[i-1] == "3" or s[i-1] == "1"):
                print("tem") #lado esquerdo
    

    elif(s[i] == "2"):
        if(s[i] != [0]):
            if(s[i-1] == "3" or  s[i-1] == "2"):
                print("tem") #lado esquerdo
    

            
            
