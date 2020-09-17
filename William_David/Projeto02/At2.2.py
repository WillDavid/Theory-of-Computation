# Título: Atividade Avaliativa 2.2
# Autor: William David Martins de Almeida
# Versão: Python Estruturado
# Casos de Teste: 10/10
# GitHub: https://github.com/WillDavid/Theory-of-Computation


pilha = []
lista = []
casado = True
correto = True
mostrarFora = []

while (True):
    correto = True
    string = str(input())

    # Quando o usuario teclar enter sem algo para input
    if string == "":
        for i in mostrarFora:
            print(i)
        break

    r = ''
    for i in string:
        r += i.replace(" ", '')

    # Se apenas tiver uma string de [Espaços]
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

       # Verifica se a String (Casada) está correta ou não
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
              
        # Verifica se ela é "Não casada" , "Casada Correta" ou "Casada Incorreta"

        if (casado == True):
            if(correto):
                print("casada e correta")
            else:
                print("casada e incorreta")

                #Lógica de organização
                    # se ([ -> [(
                    # se [{ -> {[
                    # se ({ -> {(

                    # se ]) -> )]
                    # se }] -> ]}
                    # se }) -> )}         
            
                valoresNumero = []
                for i in range(len(s)):
                    valoresNumero.append(s[i])

                
                # Ordenação da String seguindo a lógica anteriormente apresentada
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
                #Criacao da String que vai ser mostrada    
                StringTratadaFinal = ''
                for i in valoresNumero:
                    if(i == "1"):
                        StringTratadaFinal+="{"
                    if(i == "2"):
                        StringTratadaFinal+="["
                    if(i == "3"):
                        StringTratadaFinal+="("
                    if(i == "4"):
                        StringTratadaFinal+=")"
                    if(i == "5"):
                        StringTratadaFinal+="]"
                    if(i == "6"):
                        StringTratadaFinal+="}"
                
                #Essa variavel vai ser mostrada quando o programa finalizar
                mostrarFora.append(StringTratadaFinal)

                #Reseta o valores para a chegada da proxima String Casada e Incorreta
                StringTratadaFinal = ''
                valoresNumero = []        
        else:
            print("nao casada")
            casado = True
    # Reseta a Pilha e a Lista para a próxima String
    pilha = []
    lista = []