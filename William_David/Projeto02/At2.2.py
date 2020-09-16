string = "}["
pilha = []
casado = True
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
                casado = False
        else:
            casado = False

#parte 2
lista = []
for i in string:
    lista.append(i)

d = [('(', "3"), (')', "4"),('[', "2"), (']', "4"), ('{', "1"), ('}', "6")]
dicio = dict(d)

s = ''
for i in lista:
    s += dicio[i]

correto = True
for i in range(len(s)):
    if s[i] == "3":
        if s[i+1] == "1" or s[i+1] == "2":
            correto = False
            break
    elif s[i] == "2":
        if s[i+1] == "1" or s[i+1] == "6":
            correto = False
            break
    elif s[i] == "1":
        print("to vendo")
    else:
        print("nao faz nada")

if (len(pilha) == 0) and (casado == True):
    if(correto):
        print("casada e correta")
    else:
        print("casada e incorreta")
else:
    print("nao casada")

