#mini calculadora

def soma (numero1, numero2):
    resultado = numero1+numero2
    print (resultado)
    return 

def subtração (numero1, numero2):
    resultado = numero1-numero2
    print (resultado)
    return 

def divisão (numero1, numero2):
    resultado = numero1/numero2
    print (resultado)
    return 

def multiplicação (numero1, numero2):
    resultado = numero1*numero2
    print (resultado)
    return 


Escolha = int(input("Digite 1-Soma, 2-Subtração, 3-Divisão e 4-Multiplicação:"))
numero1 = float (input("Digite um número:"))
numero2 = float (input("Digite outro número:"))

if escolha == 1:
    soma(numero1,numero2)
elif escolha == 2:
    subtração(numero1,numero2)
elif escolha == 3:
    divisão(numero1,numero2)
elif escolha == 4:
    multiplicação(numero1,numero2)
else:
    print("Opção invalida")

print ("Mini calculadora")
print ("="*15)
