vogais = ["A", "E", "I", "O", "U"]

letter = input("Digite uma letra:")
newLetter = letter.upper()


print("Checking")

#if ((type(newLetter))) == <class "int">: //not working
if (newLetter.isnumeric()): 
#if (type(newLetter) != str): // not working
#if isinstance(newLetter, int): // not working
#os metodos que nao estao funcionando é porque provavelmente eu converti o input em letra maiuscula
        print("Its a number")
elif (newLetter in vogais) :
        print("A letra é uma vogal")
else:
        print("A letra é uma consoante")