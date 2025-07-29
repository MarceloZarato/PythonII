#Você é de maior ou não#

idade = int(input("Digite sua idade:"))
if idade >= 18:
    print ("Você é de maior!")
else:
    print("Você é de menor!")

#Você pode votar ou não#

idade = int(input("Digite sua idade:"))
if idade == 16:
    print("Você tem a escolha de voto ou não!")
elif idade > 16:
    print("Você tem que voto!")
else:
    print("Você não pode votar!")

#Impar ou Par#

numero = int(input("Digite um número:"))
if (numero%2==0):
    print("É par!")
else:
    print("É ímpar!")

#Laços de Repetição#

for i in range (20,2):
    print (i)
