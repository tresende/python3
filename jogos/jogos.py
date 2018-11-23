# jogos.py

import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    adivinhacao.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    forca.jogar()