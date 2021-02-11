print("**********************************")
print(" Bem vindo ao jogo da Adivinhação!")
print("**********************************")

secret_number = 42

kick_str = input("Digite o seu número: ")

print("Você digitou ", kick_str)

kick = int(kick_str)

if(secret_number == kick):
    print("Você advinhou o número secreto")
else:
    print("Você errou!")