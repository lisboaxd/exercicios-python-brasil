#condig:UTF-8
'''
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. 
'''
class Retangulo(object):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def muda_valores_lado(self):
        aux = self.altura
        self.altura = self.base
        self.base = aux
        print("mudou os valores")

    def valor_lados(self):
        return 'Base: {0:.0f}\nAltura: {1:.0f}'.format(self.base * 100, self.altura * 100)

    def calcula_area(self):
        return (self.base * self.altura) * 100

    def calcula_perimetro(self):
        return ((self.base + self.altura) * 2) * 100


base = float(input("Insira o comprimento em Metros:"))
altura = float(input("Insira a largura em Metros: "))
retan = Retangulo(base, altura)
print(retan.__dict__)
print(retan.valor_lados())
retan.muda_valores_lado()
print(retan.valor_lados())
print("Area do piso: {0:.0f}cm ou {1:.0f} metros".format(
    retan.calcula_area(),
    retan.calcula_area()/100
    )
)
print("Perimetro da area: {0:.0f}cm".format(retan.calcula_perimetro()))
