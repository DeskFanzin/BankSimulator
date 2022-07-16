class Banco:
    def __init__(self):
        self.contas = []
        
    def depositar(self, numero, valor):
        for i in range(len(self.contas)):
            if i.numero_conta == numero:
                i.saldo += valor
    
    def sacar(self, numero, valor):
        for i in range(len(self.contas)):
            if i.numero_conta == numero:
                i.saldo -= valor

    def consultar_saldo(self, numero):
        for i in range(len(self.contas)):
            if i.numero_conta == numero:
                return i.saldo

class Conta:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo
