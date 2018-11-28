class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

if (__name__ == "__main__"):
    conta = Conta('037112', 'Thiago Resende', 200, 300)
    conta.extrato()
    conta.deposita(15.0)
    conta.extrato()
    conta.saca(15.0)
    conta.extrato()