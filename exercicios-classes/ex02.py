#condig:UTF-8
'''
Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 
'''
class Quadrado(object):

    def __init__(self, tamanho):
        self.tamanho = tamanho

    def __str__(self):
        return "Valor do quadrado é: {0} ".format(self.tamanho **2)

    def mudar_valor_lado(self, valor):
        self.tamanho = valor

    def retornar_valor_lado(self):
        return self.tamanho

    def calcular_area(self):
        return self.tamanho ** 2


quad = Quadrado(4)
print(quad.retornar_valor_lado())
print(quad.calcular_area())
quad.mudar_valor_lado(2)
print(quad.retornar_valor_lado())
print(quad.calcular_area())
