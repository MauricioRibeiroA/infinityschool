  #Faça uma função para calcular o valor/hora de um funcionario
nome_funcionario = input('Qual o nome do funcionário? ')
salario = int(input('Quanto o funcionário recebeu no período? '))
horas_trab = int(input('Quantas horas o funcionário trabalhou no período? '))


def calculate_valorhora(valor_recebido: int, funcionario_name: str, horas_trabalhadas: int):
    valor_hora = valor_recebido / horas_trabalhadas
    return f'O valor hora do funcionário {funcionario_name} é de R${valor_hora}'
  
print(calculate_valorhora(salario, nome_funcionario, horas_trab))