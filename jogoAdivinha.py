print("**********************************")
print(" Bem vindo ao jogo da Adivinhação!")
print("**********************************")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou ", chute)

if(numero_secreto == chute):
    print("Você advinhou o número secreto")
else:
    print("Você errou!")