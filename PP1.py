import re


'''
Função responsavel por analisar se o texto está recebendo a primeira
e a segunda linha corretamente.
'''

def Separador(separador, status):
    if(re.search(r'^-{23}$',separador)):
        status = True
        print("Separador = True")
    else:
        status = False
        print("Separador = False")
       

def PrimeiraEUltimaLinha(begin, status):
    if(re.search(r'-{5}beginmessage-{5}',begin)):
        status = True
        print("Primeira Linha = True")
    else:
        status = False
        print("Primeira Linha = False")
        
def UltimaLinha(endi):
    if(re.search(r'^-{5}endmessage-{5}$',endi)):
        print("Ultima Linha = True")
    else:
        print("Ultima Linha = False")

   

def FromToEmailVerificacao(fromEmail):
    if(re.search(r'^from:\s+[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+\;$', fromEmail)):
        print("Verificacao From Email = True")
    else:
        print("Verificacao From Email = False")

def ToEmailVerificacao(toEmail):
    if(re.search(r'^to:\s+[a-zA-Z]+\@[a-zA-Z]+(\.[a-zA-Z]+){1,2}\;$', toEmail)):
        print("Verificacao To Email = True")
    else:
        print("Verificacao To Email = False")




    
    


 

texto = open('Entrada.txt', 'r', encoding='utf-8') 
status = True


begin = texto.readline()
fromEmail = texto.readline()
toEmail = texto.readline()
ipAutor = texto.readline()
timeStamp = texto.readline()
separador = texto.readline()
endi = texto.readline()



PrimeiraEUltimaLinha(begin, status)
FromToEmailVerificacao(fromEmail)
ToEmailVerificacao(toEmail)
UltimaLinha(endi)
Separador(separador, status)


if(status == False):
    print("spam")
elif(status == True):
    print("ham")
else:
    print("Nenhum dos dois")

texto.close() 


