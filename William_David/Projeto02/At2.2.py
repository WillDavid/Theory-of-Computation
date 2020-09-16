string = "([{}])"
pilha = []
correto = True
for i in string:
    
    if i== "(" or i=="[" or i=="{":
        pilha.append(i)
        topo = i
    else:
        if pilha != []:
            if (i == ")" and topo == "(" ) or (i=="]" and i=="[") or (i=="}" and i=="{"):    
                if len(pilha) > 0:
                    pilha.pop()
            else:
                correto = False
        else:
            correto = False
    print(pilha)             

if (len(pilha) == 0) and (correto == True):
    print("casada")
else:
    print("nao casada")



    #Se eu tenho ( )
