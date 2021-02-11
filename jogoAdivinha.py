import random

print("**********************************")
print(" Bem vindo ao jogo da Adivinhação!")
print("**********************************")

secret_number = random.randrange(1, 101)
attempts_total = 0
points = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil  (2) Médio  (3) Difícil" )

level = int(input("Defina o nível: "))

if(level == 1):
    attempts_total = 20
elif(level == 2):
    attempts_total = 10
elif(level == 3):
    attempts_total = 3

for round_attempts  in range(1, attempts_total + 1):
    print("Tentativa {} de {}".format(round_attempts, attempts_total))
    kick_str = input("Digite um número entre 1 e 100: ")
  
    kick = int(kick_str)

    if(kick < 1 or kick > 100 ):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    hit = kick == secret_number 
    its_bigger = kick > secret_number
    its_smaller = kick < secret_number

    
    if(hit):
        print("Você advinhou o número secreto. Sua pontuação final é {} pontos".format(points))
        break
    
    else:
        if(its_bigger):
            print("Você errou! O número que você digitou é maior que o número secreto.")
            if(round_attempts == attempts_total):
                loss_points = abs(secret_number - kick)
                points = points - loss_points
                print("Você não advinhou o número secreto. Sua pontuação final é {} pontos".format(points))
                break
        elif(its_smaller):
            print("Você errou! O número que você digitou é menor que o número secreto.")
            if(round_attempts == attempts_total):
                loss_points = abs(secret_number - kick)
                points = points - loss_points
                print("Você não advinhou o número secreto. Sua pontuação final é {} pontos".format(points))
                break
        loss_points = abs(secret_number - kick)
        points = points - loss_points
    
print("Fim do jogo")