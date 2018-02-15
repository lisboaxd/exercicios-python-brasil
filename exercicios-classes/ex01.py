#conding: UTF-8
'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

class Bola(object):
    
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __str__(self):
        return "Bola {0}".format(self.cor)

    def trocarCor(self, cor_nova):
        self.cor = cor_nova

    def mostraCor(self):
        print('Cor da bola é {0}'.format(self.cor))


bola = Bola('vermelha',6,'metal')

print(bola)
bola.trocarCor('preto')
print(bola)
bola.mostraCor();