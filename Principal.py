from Banco import *
from Cliente import *
from Conta import *

banco = Banco()

cliente1 = Cliente('Fulano', 24)
cliente2 = Cliente('Ciclano', 22)

conta1 = ContaCorrente(1234, 1111, 1200)
conta2 = ContaCorrente(5678, 2222, 1000)
conta3 = ContaPoupanca(1234, 3333, 800)
conta4 = ContaPoupanca(5678, 4444, 600)

cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)

banco.adicionar_cliente(cliente1)
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta3)

banco.adicionar_cliente(cliente2)
banco.adicionar_conta(conta2)
banco.adicionar_conta(conta4)

if banco.autenticar(cliente1):
    conta1.extrato()
    conta1.sacar(200)
    conta1.depositar(400)
    conta3.extrato()
    conta3.sacar(600)
else:
    print('Erro na autentificação do cliente.\n')

if banco.autenticar(cliente2):
    conta2.extrato()
    conta2.sacar(400)
    conta2.depositar(200)
    conta4.extrato()
    conta4.sacar(400)
else:
    print('Erro na autentificação do cliente.\n')
