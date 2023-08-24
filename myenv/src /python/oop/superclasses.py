""" refatorar o codigo do exericio de classes utilizando superclass """
# class Animal():
#   def __init__(self, name, breed, weight):
#     self.name = name
#     self.breed = breed
#     self.weight = weight

#   def comer_racao(self):
#     return f'croc croc croc'
  
#   def derrubar_coisas(self):
#     return f'O animal {self.name} quebrou algo'
  

# class Cachorro(Animal):
#   def __init__(self, name, breed, weight):
#     super().__init__(name, breed, weight)

# class Gato(Animal):
#   def __init__(self, name, breed, weight):
#     super().__init__(name, breed, weight)

# cachorro1 = Cachorro('Bidu', 'Poodle', 20)
# gato1 = Gato('Miau', 'Siames', 10)

# print(f'O cachorro {cachorro1.name} é da raça {cachorro1.breed}, pesa {cachorro1.weight} e come: {cachorro1.comer_racao()} e {cachorro1.derrubar_coisas()}')

# print(f'O gato {gato1.name} é da raça {gato1.breed}, pesa {gato1.weight} e {gato1.derrubar_coisas()} e come: {gato1.comer_racao()}')

""" Construir sitema bancario """
class Banco():
    def __init__(self, identificador, nome, saldo):
        self.identificador = identificador
        self.nome = nome
        self.saldo = saldo
    

    def verificar_infos(self):
        return f'Seja bem vindo {self.nome} o seu identificador é {self.identificador} e seu saldo atual é {self.saldo}'
    

    def depositar(self, valor):
        resultado = self.saldo + valor
        return resultado
    
    
class ContaCorrente(Banco):
    def __init__(self, identificador, nome, saldo):
        super().__init__(identificador, nome, saldo)
            
    def sacar(self, valor):
        resultado = self.saldo - valor
        return resultado
    
    # def criar_conta_corrente(self, identificador, nome, saldo):
    #     corrente1 = ContaCorrente(self.identificador, self.nome, self.saldo)
    #     return corrente1

corrente2 = ContaCorrente('1234', 'mau', 500)    
print(corrente2)
print(corrente2.nome)



class ContaPoupanca():
    def __init__(self, identificador, nome, saldo) -> None:
        self.juros = juros
        super().__init__(identificador, nome, saldo)


# id = input('Digite o identificador do cliente: ')
# nome = input('Digite o nome do cliente: ')
# saldo = input('Digite o saldo do cliente: ')
   

