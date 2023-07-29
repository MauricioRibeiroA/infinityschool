'''
def converter(f):
    celsius = f'{((f-32)/1.8):.6f}'
    return celsius

print(converter(32))


def converterOposto(c):
    farenheit = f'{(c*1.8+32):.4f}'
    return farenheit

print(converterOposto(32))
'''

'''
nome = 'felipe'

if nome:
    print('o valor é verdadeiro')

print(type(nome))
'''
#####################
'''
perguntas = 3
questions = []
numeros = []
while len(questions) <= perguntas:
    n = input('digite um numero: ')
    for n in questions:
        questions.append(n)
print(questions)
#numeros = [1,2,3]
###################
def bigger(numeros):
    return max(numeros)
print(bigger(numeros))
'''

##################
'''
def converter(f):
    celsius = float(f'{((f-32)/1.8):.6f}')
    print(type(celsius))
    if 20 <= celsius <= 25:
        print('saia de bermuda')
    elif 15 <= celsius <= 19:
        print('leve um casaco')
    elif 0 <= celsius <= 14:
        print ('Assista netflix e tome um café')
        
(converter(76))
'''
'''
f = float

def converter(f):
    celsius = float(f'{((f-32)/1.8):.6f}')
    match celsius:
        case 0 | 25:
            return 'bermuda'

print(converter(32))
'''
# defining method to write down the alphabet
length = 28
alphabet = []
#i = 97
'''
def writeAlphabet(i):   
    while i < (length + 97):   
        alphabet.append(i)
        i += 1
        #print(alphabet)
    
    for letter in alphabet:
        print(chr(letter))

writeAlphabet(i)

print(ord('a'))

for i in range(97, 123):
    alphabet.append(i)
    for letter in alphabet:
        alfabeto = (chr(letter))
    print(alfabeto,end=',')
'''
#
'''
numero = int(input('Digite um numero: '))

for n in range(0, numero, 2):
    print(n, end=',')
'''


#contrua um código onde você peça um número ao usuário e escreva a tabuada de 1 a 10 desse determinado número
length = 10
tabuada = []

def calcularTabuada():
    i = 1
    numero = int(input('Digite um numero: '))
    while len(tabuada) < length:
        resultado = numero * i
        tabuada.append(resultado)
        i += 1
    print(tabuada)

calcularTabuada()
