import re

pilha = []
lista = []
casado = True
correto = True
mostrarFora = []

while (True):
    correto = True
    string = str(input())

    if string == "":
        for i in mostrarFora:
            print(i)
        break

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
                '''
                elif s[i] == "1":
                    print("to vendo")
                else:
                    print("nao faz nada")
                '''
        

        #Verificacao

        if (casado == True):
            if(correto):
                print("casada e correta")
            else:
                print("casada e incorreta")

                # se ([ -> troca ok
                # se [{ -> troca ok
                # se ({ -> troca ok

                # se ]) -> troca ok
                # se }] -> troca
                # se }) -> troca ok         
            
                valoresNumero = []
                for i in range(len(s)):
                    valoresNumero.append(s[i])

                
                j = 0
                while(j<10):    
                    for i in range(len(valoresNumero)):
                            if(valoresNumero[i] == "3"):
                                aux = valoresNumero[i]
                                if(valoresNumero[i+1] == "2" or valoresNumero[i+1] == "1"):
                                    result = valoresNumero[i].replace(valoresNumero[i], valoresNumero[i+1])
                                    valoresNumero[i] = result
                                    valoresNumero[i+1] = aux
                                    
                            
                            if(valoresNumero[i] == "2"):
                                aux = valoresNumero[i]
                                if(valoresNumero[i+1] == "1"):
                                    result = valoresNumero[i].replace(valoresNumero[i], valoresNumero[i+1])
                                    valoresNumero[i] = result
                                    valoresNumero[i+1] = aux

                            if(valoresNumero[i] == "5"):
                                aux = valoresNumero[i]
                                if(valoresNumero[i-1] == "6"):
                                    result = valoresNumero[i].replace(valoresNumero[i], valoresNumero[i-1])
                                    valoresNumero[i] = result
                                    valoresNumero[i-1] = aux
                                    
                                
                            if(valoresNumero[i] == "4"):
                                aux = valoresNumero[i]
                                if(valoresNumero[i-1] == "6" or valoresNumero[i-1] == "5"):
                                    result = valoresNumero[i].replace(valoresNumero[i], valoresNumero[i-1])
                                    valoresNumero[i] = result
                                    valoresNumero[i-1] = aux
                    j=j+1
                        
                        

                        

                        

                        
                                
                        
                    
                        
                vetorFinal = ''
                for i in valoresNumero:
                    if(i == "1"):
                        vetorFinal+="{"
                    if(i == "2"):
                        vetorFinal+="["
                    if(i == "3"):
                        vetorFinal+="("
                    if(i == "4"):
                        vetorFinal+=")"
                    if(i == "5"):
                        vetorFinal+="]"
                    if(i == "6"):
                        vetorFinal+="}"

              

                
                mostrarFora.append(vetorFinal)

                vetorFinal = ''
                valoresNumero = []

                


                

                    
        else:
            print("nao casada")
            casado = True

    pilha = []
    lista = []


    
 





