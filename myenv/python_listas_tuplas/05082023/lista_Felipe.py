#Crie uma lista, com os seus dados de nome, idade e altura, porém, eles precisam estar errados, por exemplo:
infosUsuarios = ['mauricio', 'ribeiro', 'infinity', 'sabado']

def perguntaAluno():
    print(infosUsuarios)
    question = input('os dados inseridos estão corretos? S ou N ').upper()
    if question == 'S':
        return True
    else:
       newQuestion = input('O que esta errado?' )
       posicaoInfo = infosUsuarios.index(newQuestion)
       newElement = input('Por qual info gostaria de substituir? ')
       infosUsuarios[posicaoInfo] = newElement
       print(f'Certo! Pedimos desculpas pelo transtorno. Seguem novos dados: {infosUsuarios}')
perguntaAluno()


