import random

numero_secreto = random.randint(1,100)
print(numero_secreto)

print("Bem-vindo ao jogo!")

tentativas = 0 

acertou = False

while not acertou:
    palpite = int(input("Digite um numero: "))

    if palpite == numero_secreto:
     print("Parabens voce acertou!")

    elif palpite < numero_secreto:
     print("Numero muito baixo")

    else:
     print("Numero muito alto!")





