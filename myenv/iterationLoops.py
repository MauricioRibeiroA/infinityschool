conjunto = (2,3,4,5,6)

for i in conjunto:
    if i % 2 == 0:
        print(f'o número {i} é par')
    else:
        print(f'o número {i} é ímpar')
################################################
for i in conjunto:
    if i % 2 == 0:
        print(f'o número {i} é par')
        break
else:
    print('foi encontrado um número ímpar')
################################################
for i in conjunto:
    if i % 2 == 0:
        print(f'aqui temos  o número {i} que é par')
        continue
    else:
        print(i)
        break
else:
    print('encontramos um número ímpar e precisamos encerrar o loop')
################################################
for i in conjunto:
    if i % 2 == 0:
        print(f'aqui temos  o número {i} que é par')
        continue
    else:
        print(i)
################################################
for i in conjunto:
    if i % 2 == 0:
        pass #escrever código posteriormente
    else:
        print(i)        

    