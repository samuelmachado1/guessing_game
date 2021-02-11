print("**********************************")
print(" Bem vindo ao jogo da Adivinhação!")
print("**********************************")

secret_number = 42
attempts_total = 3
round_attempts = 1

while(round_attempts <= attempts_total):
    print("Tentativa ", round_attempts, " de ", attempts_total )
    kick_str = input("Digite o seu número: ")

    print("Você digitou ", kick_str)

    kick = int(kick_str)

    hit = kick == secret_number 
    its_bigger = kick > secret_number
    its_smaller = kick < secret_number

    if(hit):
        print("Você advinhou o número secreto")
    else:
        if(its_bigger):
            print("Você errou! O número que você digitou é maior que o número secreto.")
        elif(its_smaller):
            print("Você errou! O número que você digitou é menor que o número secreto.")

    round_attempts = round_attempts + 1
print("Fim do jogo")