import math
#Escreva uma função que receba um número e verifique se ele é primo

#verificar com algoritmo Big O
def its_prime(num: int):
  for i in range(2, int(math.sqrt(num) + 1)):
    if num % i == 0:
       return "O número não é primo."
    return 'O número consultado é primo'

print(its_prime(4))