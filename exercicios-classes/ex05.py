'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios. '''

class Corrente(object):

    def __init__(self,numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return "Nome:{nome}\nNumero:{numero}\nSaldo:{saldo:.2f}\n\n"\
        .format(
            nome = self.nome,
            numero = self.numero,
            saldo = self.saldo
            )

    def alterarNome(self, nome):
        self.nome = nome

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

c = Corrente('3144124-1','Mateus Lisboa',504.5)
print(c)
c.alterarNome('Jose Antonio')
print(c)
c.deposito(54.1)
print(c)
c.sacar(42)
print(c)