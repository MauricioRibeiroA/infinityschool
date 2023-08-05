'''num = int(input('Digite um número: '))

if num == 3:
    print('numeros iguais')
elif num ==2:
    print('numeros quase iguais')
else:
    print('numeros bem diferentes')'''

################################################

#if em uma linha de código 
'''vendas = 1000

if vendas > 500:
    bonus = 50
else:
    bonus = 0

print(bonus)'''
#(ternary operator)
'''vendas = 1000
bonus = 50 if vendas > 500 else 0
#variavel = valor_se_verdadeiro if condicao else valor se falso
print(bonus)'''

def ganhou_bonus(vendas):
    if vendas > 500:
        return True
    else:
        return f'Faltou {500 - vendas} unidades'
print(ganhou_bonus(100))

#(ternary operator)
def ganhou_bonus2(vendas):
    return vendas > 500 or f'Faltou {500 - vendas} unidades'
print(ganhou_bonus2(1030))