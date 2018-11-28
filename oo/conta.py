class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


if (__name__ == "__main__"):
    conta = Conta('037112', 'Thiago', 200, 300)
    conta2 = Conta('912832', 'Camila', 400, 300)
    conta.limite = 1000.0
    print(conta.saldo)
    conta2.transfere(10, conta)

    conta.extrato()
    conta2.extrato()
