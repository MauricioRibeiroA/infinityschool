infos = ['nome', 'nota1', 'nota2', 'nota3', 'nota4', 'menor_nota', 'maior_nota', 'situacao', 'status']

novas_infos = dict.fromkeys(infos)

for i in range(0, 2):
  def get_infos_method():
    novas_infos['nome'] = input('Digite o seu nome: ')
    novas_infos['nota1'] = int(input('Digite sua primeira nota: '))
    novas_infos['nota2'] = int(input('Digite sua segunda nota: '))
    novas_infos['nota3'] = int(input('Digite sua terceira nota: '))
    novas_infos['nota4'] = int(input('Digite sua quarta nota: '))
    return novas_infos
  get_infos_method()

def setting_name_as_data_index():
  chaves_index_nome = list(novas_infos.keys())[0]
  return chaves_index_nome
index_name = setting_name_as_data_index()
print(index_name)

def creating_notas_array():
  notas = [novas_infos['nota1'], novas_infos['nota2'], novas_infos['nota3'], novas_infos['nota4']]
  return notas
conjunto_notas = creating_notas_array()

def calculate_max_grade():
  notas = [novas_infos['nota1'], novas_infos['nota2'], novas_infos['nota3'], novas_infos['nota4']]
  max_grade = __builtins__.max(notas) 
  return max_grade
maior_nota = calculate_max_grade()

def calculate_min_grade():
  notas = [novas_infos['nota1'], novas_infos['nota2'], novas_infos['nota3'], novas_infos['nota4']]
  min_grade = __builtins__.min(notas) 
  return min_grade
menor_nota = calculate_min_grade() 

def calculate_average_grade():
  notas = [novas_infos['nota1'], novas_infos['nota2'], novas_infos['nota3'], novas_infos['nota4']]
  grades_sum = __builtins__.sum(notas)
  average_grade = grades_sum / len(notas)
  return average_grade
media_aluno = calculate_average_grade()

def defining_situacao():
  if media_aluno >= 7:
    return 'Aprovado'
  else:
    return 'Reprovado'
situacao_aluno = defining_situacao()

def msg_estimulo():
  if situacao_aluno == 'Aprovado':
    return 'Parabéns!'
  else:
    return 'Acreditamos no seu potencial e nos vemos no próximo curso'
mensagem_aluno = msg_estimulo()

for i in novas_infos:
  print(i)

def historico_aluno(arg1):
   print(f'Este é o histórico escolar do aluno: {novas_infos[arg1]}')
   print(f'O nome do aluno é: {novas_infos[index_name]}')
   print(f'As suas notas no período letivo foram: {conjunto_notas}. Sendo que sua maior nota foi {maior_nota} e a sua menor nota foi {menor_nota}')
   print(f'A sua média durante o ano letivo foi: {media_aluno}, portanto você está {situacao_aluno}.{mensagem_aluno}')
   print('-'*30)
#historico_aluno('nome')


