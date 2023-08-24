""" primeira apostila """
# class Fatura():
#     def __init__(self, name, unit_price, quantidade, total_value):
#         self.name = name
#         self.unit_price = unit_price
#         self.quantidade = quantidade
#         self.total_value = total_value

    
#     def Gerar_fatura(self):
#         resultado = self.quantidade * self.unit_price
#         return resultado


# fatura_1 = Fatura('mauricio', 1000, 1, 3000)
# fatura_2 = Fatura('mauricio', 300, 1, 3000)


""" segunda apostila 1 atividade """
# class Cachorro():
#     def __init__(self, name, breed, weight) -> None:
#         self.name = name
#         self.breed = breed
#         self.weight = weight
    

#     def comer_racao(self):
#         return f'croc croc croc'

# cachorro1 = Cachorro('Bidu', 'Poodle', 20)
# cachorro2 = Cachorro('Floquinho', 'Maltes', 25)

# print(f'O cachorro {cachorro1.name} é da raça {cachorro1.breed}, pesa {cachorro1.weight} e come: {cachorro1.comer_racao()}')

# print(f'O cachorro {cachorro2.name} é da raça {cachorro2.breed}, pesa {cachorro2.weight} e come: {cachorro2.comer_racao()}')

""" segunda apostila 2 atividade """
class Gato():
    def __init__(self, name, breed, weight) -> None:
          self.name = name
          self.breed = breed
          self.weight = weight

    def derrubar_coisas(self):
         return f'O gato {self.name} quebrou algo'
    
gato1 = Gato('Miau', 'Siames', 10)
print(f'O gato {gato1.name} é da raça {gato1.breed}, pesa {gato1.weight} e {gato1.derrubar_coisas()}')