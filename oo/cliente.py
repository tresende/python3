class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome


if (__name__ == "__main__"):
    # from cliente import Cliente
    cliente = Cliente('Thiago')
    cliente.nome = "Thiago Resende"
    print(cliente.nome)
