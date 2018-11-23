# jogos.py

import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")
    print("(1) Adivinhação (2) Forca")
    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        adivinhacao.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        forca.jogar()


if (__name__ == "__main__"):
    escolhe_jogo()
