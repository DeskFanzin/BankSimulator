import random

class Conta:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo
    def __repr__(self):
        return str(self.numero_conta)

class Banco:
    def __init__(self):
        self.contas = {}
        self.chaves = []
    
    def __repr__(self):
            return str(self.contas)

    def cria_conta(self, numero_contas):
        for i in range(numero_contas):
            numero = random.randint(1, 100)
            saldo = random.randint(0, 100)
            self.contas[numero] = saldo
        for key in self.contas:
            self.chaves.append(key)

    def depositar(self, numero, valor):
        for i in range(len(self.contas)):
            if self.chaves[i] == numero:
                self.contas[numero] += valor
    
    def sacar(self, numero, valor):
        for i in range(len(self.contas)):
            if self.chaves[i] == numero:
                self.contas[numero] -= valor

    def consultar_saldo(self, numero):
        for i in range(len(self.contas)):
            if self.chaves[i] == numero:
                return self.contas[numero]
