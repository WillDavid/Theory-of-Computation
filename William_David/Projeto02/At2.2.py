string = "(())()())"


pilha = []

for i in string:
    print(pilha)
    if i== "(" or i=="[" or i=="{":
        pilha.append(i)
    else:
        topo = pilha[-1]
        if (i == ")" and topo == "(") or (i=="]" and topo == "[") or (i=="}" and topo == "{"):
            pilha.pop()
            status = True
        else:
            status = False
            break
            
        

if status == True:
    print("casada")
else:
    print("nao casada")


