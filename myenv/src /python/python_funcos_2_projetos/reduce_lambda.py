from functools import reduce

numeros = [1,2,3,4,5]
soma = reduce(lambda num1, num2: num1 + num2, numeros)
print(soma)