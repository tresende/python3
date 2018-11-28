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


if (__name__ == "__main__"):
    conta = Conta('037112', 'Thiago Resende', 200, 300)

    conta2 = conta
    conta2.__saldo = 99999999
    conta2 = None
    
    conta.extrato()
    conta.deposita(15.0)
    conta.extrato()
    conta.saca(15.0)
    conta.extrato()
