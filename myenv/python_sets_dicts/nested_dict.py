#criando o dicionario principal chamado nested students
nested_students = dict()

#criando o dicionario secundario que será populado com os dados dos estudantes e ficará dentro do dicionário principal
dados = ['nome', 'sobrenome', 'idade']
students = dict.fromkeys(dados)


#how to access student1 key

#how to access student1 values

#CRUD
#testando como criar uma chave dentro do grupo principal nested students
nested_students['student1'] = students



#how to acsess student1
def access_one_student(student_position):
    print(f'esses são os dados do {student_position} {nested_students[student_position]}')
access_one_student('student1')


#CREATE
def create_student(student_name):
    nested_students[student_name] = {}
create_student('student2')

for student in nested_students:
    nested_students[student] = students

#READ
def show_one_student():
    pass

def show_all_students():
    pass

#UPDATE
def update_specific_student(student_name, key_name, value_name):
    nested_students[student_name][key_name] = value_name
update_specific_student('student1', 'nome', 'mauricio')
print(nested_students)
#DELETE
def delete_student():
    pass