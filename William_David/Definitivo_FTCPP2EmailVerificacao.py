import re

# 18/08/2020
# FTC - Atividade Avaliativa 02
# Script desenvolvido com parceria de William David e Leticia Minelvino

# Autor da Versão: William David Martins de Almeida

# Link para a versão dos dois autores: https://github.com/WillDavid/Theory-of-Computation

def Separador(separador):
    if(re.search(r'^-{23}$',separador)):
        return 1
    else:
        return 0
        
def PrimeiraEUltimaLinha(begin):
    if(re.search(r'-{5}beginmessage-{5}',begin)):
        return 1
    else:
        return 0
               
def FromToEmailVerificacao(fromEmail):
    if(re.search(r'from: (.+).*\@[\w\.]+;$', fromEmail)):
        
        return 1
    else:
        return 0
       
def ToEmailVerificacao(toEmail):
    if(re.search(r'to: (.+).*\@[\w\.]+;$', toEmail)):
        return 1
    else:
        return 0
        
def IpAutor(ipAutor):
    if(re.search(r'(\d+\.){3}\d+',ipAutor)):
        return 1
    else:
        return 0

def timeStampCheck(timeStamp):
    if(re.search(r'^\d{4}\.\d{2}.\d{2} \d{2}:\d{2}:\d{2}$', timeStamp)):
        return 1
    else:
        return 0
        
'''    Corpo da mensagem - Trecho desenvolvido por Leticia Minelvino                                                   '''

def checarEmail(escopo):
    if(re.search(r'(.+).*\@[\w\.]+', escopo)):
        return 1
    else:
        return 0
        
def checarHTML(escopo):
    if(re.search(r'<.+>|<\/.+>', escopo)):
        return 1
    else:
        return 0

def checarPalavras(escopo):
    if(re.search(r'milionario|emprestimo|loteria|banco|heranca|seguidor|desconto',escopo, flags = re.I)):
        return 1
    else:
        return 0

def checarQuantidadePontuacao(escopo):
    quantidade = re.findall(r'\;|\,|\.', escopo)
    if(len(quantidade) >= 15):
        return 1
    else:
        return 0
        
# Função desenvolvida por Leticia Minelvino
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
# Pode-se analisar com mais cuidado na versão dela no GitHub
def UltimaLinha(escopo):
    if(re.search(r'(-){5}endmessage(-){5}',escopo)):
        return 0
    else:
        return 1


#Entrada
arquivo = str(input().strip("\r"))
with open(arquivo, 'r') as texto:
    lista = []

    
    #Chamada de funções

    begin = texto.readline()
    lista.append(PrimeiraEUltimaLinha(begin))

    fromEmail = texto.readline()
    lista.append(FromToEmailVerificacao(fromEmail))

    toEmail = texto.readline()
    lista.append(ToEmailVerificacao(toEmail))

    ipAutor = texto.readline()
    lista.append(IpAutor(ipAutor))

    timeStamp = texto.readline()
    lista.append(timeStampCheck(timeStamp))

    separador = texto.readline()
    lista.append(Separador(separador))

    if 0 in lista:
        print("spam")
    
    else:
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


