num_1 = input('Digite o primeiro número: ')
num_2 = input('Digite o segundo número: ')

while num_1 == num_2:
    print('Por favor, escolha números diferentes')
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')

def biggest_number_if_statements(num_1: int, num_2: int):
    '''Recebe dois números como argumentos e retorna o maior entre eles utilizando condicionais'''
    if num_1 > num_2:
        return f'O maior número entre os dois é o {num_1}'
    elif num_1 < num_2:
        return f'O maior número entre os dois é o {num_2}'
print(biggest_number_if_statements(num_1, num_2))



def biggest_number_max_method(num_1: int, num_2: int):
    '''Recebe dois números como argumentos e retorna o maior entre eles utilizando a função max'''
    big_num = max(num_1, num_2)
    return f'O maior número entre ambos é o {big_num}'
print(biggest_number_max_method(num_1, num_2))
