num1 = int(input("Qual o primeiro numero?"))
num2 = int(input("Qual o segundo numero?"))
operador = input("Qual operação deseja realizar?")

def operacao(element1, element2, symbol):
    if (symbol == "soma"):
        return element1 + element2
    elif symbol == "subtracao":
        return element1 - element2
    elif symbol == "divisão":
        return element1 / element2
    elif symbol == "multiplicação":
        return element1 * element2 

resultado = operacao(num1, num2, operador)


def e_positivo(element):
    if element > 0:
        print("Este número é positivo")
    elif element < 0:
        print("Este número é negativo")
    else:
        print("O número escolhido não é positivo nem negativo") 

def e_par(numero):
    if numero % 2 ==0:
        print("O número é par")

print("o resultado foi", resultado)
e_par(resultado)
e_positivo(resultado)
print(f'o numero é: {type(resultado)}')

