def cria_conta(numero, titulo, saldo, limite):
    conta = {"numero": numero, "titular": titulo,
             "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))
