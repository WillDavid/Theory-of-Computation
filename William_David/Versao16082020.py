import re


'''
Função responsavel por analisar se o texto está recebendo a primeira
e a segunda linha corretamente.
'''

def Separador(separador, status):
    if(re.search(r'^-{23}$',separador)):
        status=status+1
        print(status)
        print("Separador = True")
        return 1
    else:
        
        print("Separador = False")
       

def PrimeiraEUltimaLinha(begin, status):
    if(re.search(r'-{5}beginmessage-{5}',begin)):
        status=status+1
        print(status)
        print("Primeira Linha = True")
        return 1
        
    else:
        
        print("Primeira Linha = False")
        

       

   

def FromToEmailVerificacao(fromEmail,status):
    if(re.search(r'^from:\s+[a-zA-Z0-9]+\@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}\;$', fromEmail)):
        print("Verificacao From Email = True")
        status=status+1
        return 1
    else:
        print("Verificacao From Email = False")
       

def ToEmailVerificacao(toEmail,status):
    if(re.search(r'^to:\s+[a-zA-Z0-9]+\@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}\;$', toEmail)):
        return 1
    else:
        print("Verificacao To Email = False")
        

def IpAutor(ipAutor,status):
    if(re.search(r'(\d+\.){3}\d+',ipAutor)):
        print("Teste ip = True")
        return 1
        status=status+1
    else:
        print("Hello1")

def timeStampCheck(timeStamp,status):
    if(re.search(r'^\d{4}\.\d{2}.\d{2} \d{2}:\d{2}:\d{2}$', timeStamp)):
        print("Time skip= true")
        status=status+1
        return 1
    else:
        print("Hello2")
        return 0
        
'''    Corpo da mensagem - Baseado no código de Leticia Minelvino                                                   '''

def checarEmail(escopo):
    if(re.search(r'(.+).*\@[\w\.]+', escopo)):
        return 0
    else:
        return 1


def checarHTML(escopo):
    if(re.search(r'<.+>|<\/.+>', escopo)):
        return 0
    else:
        return 1


def checarPalavras(escopo):
    if(re.search(r'milionario|emprestimo|loteria|banco|heranca|seguidor|desconto', escopo)):
        return 0
    else:
        return 1


def checarQuantidadePontuacao(escopo):
    quantidade = re.findall(r'\;|\,|\.', escopo)
    if(len(quantidade) <= 15):
        return 0
    else:
        return 1


def checarConsoantes(escopo):
    todasPalavras = escopo.split()
    todasPalavras.pop()
    for palavra in todasPalavras:
        consoantes = len(re.findall(r'b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z', palavra, flags = re.I))
        vogais= len(re.findall(r'a|e|i|o|u', palavra, flags = re.I))
        if((consoantes + vogais) > 11):
            if(consoantes > vogais):
                return 1
            else:
                return 0


def UltimaLinha(escopo):
    if(re.search(r'(-){5}endmessage(-){5}',escopo)):
        print("Ultima Linha = True")
        return 0
    else:
        print("Ultima Linha = False")
        return 1
    


        
texto = open('Entrada.txt', 'r', encoding='utf-8')

lista = []
status = 0
    


begin = texto.readline()
lista.append(PrimeiraEUltimaLinha(begin, status))

fromEmail = texto.readline()
lista.append(FromToEmailVerificacao(fromEmail,status))

toEmail = texto.readline()
lista.append(ToEmailVerificacao(toEmail, status))

ipAutor = texto.readline()
lista.append(IpAutor(ipAutor, status))

timeStamp = texto.readline()
lista.append(timeStampCheck(timeStamp, status))

separador = texto.readline()
lista.append(Separador(separador, status))
if 0 in lista:
    print("spam")
    
else:
    print("ham")
    lista = []
    escopoTexto = texto.read()
    escopo = ''.join(escopoTexto)
    lista.append(checarEmail(escopo))
    lista.append(checarHTML(escopo))
    lista.append(checarPalavras(escopo))
    lista.append(checarQuantidadePontuacao(escopo))
    lista.append(checarConsoantes(escopo))
    lista.append(UltimaLinha(escopo))

    for i in lista:
        print(lista[i])

        
    if 0 in lista:
        print("spam")
        
    else:
        print("ham")



    


    
    















texto.close() 


