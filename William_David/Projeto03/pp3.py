def mod(first, second):
    mod = first%second
    print(mod)

def verificacao(string):
    state = True
    c = 0
    for i in range(len(string)):
        if(string[i] == "#"):
            c += 1
    for i in range(len(string)):
        if(string[i-1] == "#" or string[0] == "#" or c!=1):
            state = False
        else:
            state = True
    return state

string = "IIII#III#III"
stateMachine = True
firstCount = 0
secondCount = 0

verificacao = verificacao(string)

print(verificacao)
if(verificacao == True):
    for i in string:
        if(i == "#"):
            stateMachine = False
        elif(stateMachine == True):
            firstCount += 1
        else:
            secondCount += 1

if(verificacao == True):
    mod(firstCount, secondCount)