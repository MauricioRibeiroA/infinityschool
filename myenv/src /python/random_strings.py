#Crie uma função que invente uma string e a retorna de trás para frente.

import random
import string


def reverse_string():
  random_string = random.choices(string.ascii_letters)


print(random_string)