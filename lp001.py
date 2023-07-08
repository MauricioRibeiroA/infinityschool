name = "mauricio"
surname = "ribeiro"

print(f"meu nome é {name} {surname}")


def qual_idade():
    user_age = input("qual sua idade?")
    print(user_age)
qual_idade()

def idade_nome_separados():
    user_age1 = input("insira sua idade: ")
    user_name1 = input("insira o seu nome: ")
    print(f"{user_age1} \n {user_name1}")
    
idade_nome_separados()

user_age2 = input("insira sua idade: ")
user_name2 = input("insira o seu nome: ")

print(f"{user_age2} {user_name2}")

def soma(element1, element2):
    resultado = element1 + element2
    return resultado

soma(2, 4)

def sub(element1, element2):
    resultado = element1 - element2
    return resultado

sub(10, 4)