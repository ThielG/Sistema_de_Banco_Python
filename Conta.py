from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print('Deposito realizado com sucesso.\n')
    
    @abstractmethod
    def sacar(self, valor):
        pass

    def extrato(self):
        print('-' * 40)
        print(f'\nExtrato:\n\nNúmero da agência: {self.agencia}. \nNúmero da conta: {self.numero}. \n\nValor total do saldo: R$ {self.saldo}. \n')
        print('-' * 40)


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente, tente novamente.\n')
            return
        elif self.saldo >= valor:
            self.saldo -= valor
            print('\nSaque realizado com sucesso.')
            self.extrato


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite = 4000):
        super().__init__(agencia, numero, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente, tente novamente.\n')
            return # <- talvez dê merda aqui
        elif self.saldo >= valor:
            self.saldo -= valor
            print('\nSaque realizado com sucesso.')
            self.extrato
