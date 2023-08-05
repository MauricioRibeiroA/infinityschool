import math
from operator import concat
#num = int(input('Por favor, digite um número: '))
#numerador = 4
'''
for num in range(1, num+1):
    denominador = num
    print(f'o numerador é {numerador}')
    print(f'o denominador é {denominador}')
    resultado = numerador % denominador
    if resultado == 0:
        print(f'na divisão de {numerador} por {denominador} o é resto zero')
    else:
        print(f'na divisão de {numerador} por {denominador} o resto não é zero')
'''

##### algoritmo visando Big O
'''
num = int(input('Por favor, digite um número: '))
def itsPrime(num):
#garantir que o input não seja menor ou igual a 1    
    if num <= 1:
        return 'O número não é primo.'
    
#verificar com algoritmo Big O

    for i in range(2, int(math.sqrt(num) + 1)):
      if num % i == 0:
         return "O número não é primo."
    return 'O número consultado é primo'

print(itsPrime(num))
'''
'''
conjunto = []
def solution(number):
   if number < 0:
      return 0
   for i in range(0, number):
      if i % 3 == 0 or i % 5 == 0:
         conjunto.append(i)
   resultado = sum(conjunto)
   return resultado
   #print(f'o resultado da soma dos múltiplos de 3 e 5 é: {resultado}')
print(solution(16))
'''
'''
#list comprehension
meus_numeros = [1, 56, 342, 12, 781, 23, 43, 45, 123, 567]

nova_lista = [numero for numero in meus_numeros if numero % 3 == 0]

print(nova_lista)
'''
