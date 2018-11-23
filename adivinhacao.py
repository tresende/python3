print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 43
chute = input("Digite o seu número: ")
chute = int(chute)
print("você digitou", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
print("Fim do jogo")