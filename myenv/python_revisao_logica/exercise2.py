userInput = input("Digite uma letra:")

if userInput == "f" or userInput == "F":
    print(userInput.upper(), " - Feminino")
elif userInput == "m" or userInput == "M":
    print(userInput.upper(), " - Masculino")
else:
    print("Sexo Inválido")