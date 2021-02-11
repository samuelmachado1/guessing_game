print("**********************************")
print(" Bem vindo ao jogo da Adivinhação!")
print("**********************************")

secret_number = 42
attempts_total = 3

for round_attempts  in range(1, attempts_total + 1):
    print("Tentativa {} de {}".format(round_attempts, attempts_total))
    kick_str = input("Digite um número entre 1 e 100: ")

    print("Você digitou ", kick_str)

    kick = int(kick_str)

    if(kick < 1 or kick > 100 ):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    hit = kick == secret_number 
    its_bigger = kick > secret_number
    its_smaller = kick < secret_number

    if(hit):
        print("Você advinhou o número secreto")
        break
    else:
        if(its_bigger):
            print("Você errou! O número que você digitou é maior que o número secreto.")
        elif(its_smaller):
            print("Você errou! O número que você digitou é menor que o número secreto.")
    
print("Fim do jogo")