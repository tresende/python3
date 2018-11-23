#!/usr/bin/python
# -*- coding: utf-8 -*-

print("*********************************\n\n")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 43
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa ", rodada, " de", total_de_tentativas)
    chute = input("Digite o seu número: ")
    chute = int(chute)
    print("você digitou: ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(numero_secreto == chute):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    rodada = rodada + 1

print("*********************************")
print("Fim do jogo")
print("*********************************")
