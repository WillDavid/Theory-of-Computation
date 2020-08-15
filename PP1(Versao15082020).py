import re


'''
Função responsavel por analisar se o texto está recebendo a primeira
e a segunda linha corretamente.
'''

def PrimeiraEUltimaLinha(begin, end):
    if(re.search(r'-{5}beginmessage-{5}',begin)):
        print("Primeira Linha= True")
        
    else:
        print("Primeira Linha = False")
        


    if(re.findall(r'––––-endmessage––––-',end)):
        print("Ultima Linha = True")
        
    else:
        print("Ultima Linha = False")
        









texto = open('Entrada.txt', 'r', encoding='utf-8') #Terceiro parametro = Tratamento de caracteres especiais


begin = texto.readline() #Fatiar a primeira linha da mensagem
end = texto.readline()  #Fatiar a linha seguinte (modificar depois)

PrimeiraEUltimaLinha(begin,end) #Chamada da função

texto.close() #Fechamento do texto


