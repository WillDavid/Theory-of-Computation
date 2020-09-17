import re
string = "{({[[()]]})}"
pilha = []
lista = []
casado = True
correto = True


           



#tratamento de espaço em branco
r = ''
for i in string:
    r += i.replace(" ", '')

if(len(r) == 0):
    print("casada e correta")
else:
    string = r
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

    if (len(pilha) != 0):
        casado = False





        
    #parte 2

    for i in string:
        lista.append(i)
    d = [('(', "3"), (')', "4"),('[', "2"), (']', "5"), ('{', "1"), ('}', "6")]
    dicio = dict(d)

    s = ''
    for i in lista:
        s += dicio[i]

    for i in range(len(s)):
        if casado:
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

    

    #Verificacao

    if (len(pilha) == 0) and (casado == True):
        if(correto):
            print("casada e correta")
        else:
            print("casada e incorreta")

            # se ([ -> troca
            # se [{ -> troca
            # se ({ -> troca

            # se )] -> troca
            # se [) -> troca
            # se }) -> troca
            

            
            #trabalhando nessa parte
            '''
            if(m[i] == "3"):
                    print("Entrou aqui")
                    if(m[i+1] == "2" or m[i+1] == "1"):
                        aux = 

            
            for i in range(len(m)):
                if(m[i] == "3"):
                    print("Entrou aqui")
                    if(m[i+1] == "2" or m[i+1] == "1"):
                        aux = 

                        print(aux)   
                            
        
            valoresNumero = []

            #Trabalhando nessa parte
            for i in range(len(s)):
                valoresNumero.append(s[i])

            print(valoresNumero)
            result = sorted(valoresNumero)
            print(result)  

            '''      
    else:
        print("nao casada") 





