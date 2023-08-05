#listas
#tuplas
dados_de_contato = ('Will', 'Silva', 26, 'will@email.com')

#print(type(dados_de_contato))

turma =315
modulo = 'python'
instituicao = 'infinity school'

#print(turma, modulo)
nome, _, idade, _ = dados_de_contato
#print(dados_de_contato)
info = turma, modulo, instituicao

#print(type(info))

#print(info)

#expressao estrelada
nome, sobrenome, *demais_info = dados_de_contato

print(nome, sobrenome)
print(type(demais_info))
print(demais_info)