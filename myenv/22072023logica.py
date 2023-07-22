def perguntarSenha():
    sen1 = input('Digite sua senha: ')
    sen2 = input('Confirme sua senha: ')
    while sen1 != sen2:
        print('Senhas não conferem')
        perguntarSenha()
perguntarSenha()
print('''
      Login sendo 
       efetuado!
''')

nome = input('Digite seu nome: ')

while True:
    sen1 = input('Digite sua senha: ')
    sen2 = input('Confirme sua senha: ')
    if sen1 == sen2:
        print(f'Hello {nome}, seja bem vindo!')
        break
    else:
        continue

for i in range(1, 11):
    print(i, end=',')

for i in reversed(range(-10, 11)):
    print(i, end=',')

count = 0

while count < 10:
    count +=1
    if count == 6:
        break
else:
    print(count)


count = 0 

while count < 100:
    count += 1
    if count == 55:
        count += 1
        print('Eu não quero esse número')
        #print('\033[55')
        continue
    else:
        print(f'Contador = {count}')

while True:
    nome1 = input('Digite o nome: ')
    nome2 = input('Digite o nome: ')
    if nome1 == nome2:
        print('Os nomes são iguais')
        break
    else:
        continue

listaTeste  = ['mauricio', 'ribeiro']

sorted(listaTeste, reverse=True)

listaTeste.sort(reverse=True)
print(listaTeste)
