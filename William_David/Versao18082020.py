import re


'''
Função responsavel por analisar se o texto está recebendo a primeira
e a segunda linha corretamente.
'''

def Separador(separador, status):
    if(re.search(r'^-{23}$',separador)):
        print("Separador = True")
        return 1
    else:
        print("Separador = False")
        return 0
        
       

def PrimeiraEUltimaLinha(begin, status):
    if(re.search(r'-{5}beginmessage-{5}',begin)):
        return 1
        
    else:
        print("Primeira Linha = False")
        return 0
        
        

def FromToEmailVerificacao(fromEmail,status):
    if(re.search(r'^from:\s+[a-zA-Z0-9]+\@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}\;$', fromEmail)):
        return 1
    else:
        return 0
       

def ToEmailVerificacao(toEmail,status):
    if(re.search(r'^to:\s+[a-zA-Z0-9]+\@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){1,2}\;$', toEmail)):
        print("Verificacao TO email = True")
        return 1
    else:
        print("Verificacao To Email = False")
        return 0
        

def IpAutor(ipAutor,status):
    if(re.search(r'(\d+\.){3}\d+',ipAutor)):
        print("Teste ip = True")
        return 1
        status=status+1
    else:
        print("Hello1")
        return 0

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
        print("contem um email = spam")
        return 1
    else:
        print("n contem um email = ham")
        return 0
        


def checarHTML(escopo):
    if(re.search(r'<.+>|<\/.+>', escopo)):
        print("Contem uma tag = spam")
        return 1
    else:
        print("Nao contem um tag = ham")
        return 0
        


def checarPalavras(escopo):
    if(re.search(r'milionario|emprestimo|loteria|banco|heranca|seguidor|desconto',escopo, flags = re.I)):
        print("contem a palavra = spam")
        return 1
    else:
        print("nao contem a pavara = ham")
        return 0
        


def checarQuantidadePontuacao(escopo):
    quantidade = re.findall(r'\;|\,|\.', escopo)
    if(len(quantidade) >= 15):
        print("Maior que 15 = spam")
        return 1
    else:
        print("menor que 15 = ham")
        return 0
        


def checarConsoantes(escopo):
    conjuntoPalavras = escopo.split()
    conjuntoPalavras.pop()
    for palavras in conjuntoPalavras :
        consoantes = len(re.findall(r'b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z', palavras, flags = re.I))
        vogais = len(re.findall(r'a|e|i|o|u', palavras, flags = re.I))
        if((consoantes + vogais) > 11):
            if(consoantes > vogais):
                return 1
            else:
                return 0


def UltimaLinha(escopo):
    if(re.search(r'(-){5}endmessage(-){5}',escopo)):
        print("Contem os - no final = ham")
        return 0
    else:
        print("n contem travsao no final = spam1")
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


if 1 in lista:
    print("spam")
        
else:
    print("ham")



    


    
    















texto.close() 


