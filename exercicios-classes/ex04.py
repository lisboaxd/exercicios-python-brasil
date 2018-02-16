'''Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm. '''

class Pessoa(object):

    def __init__(self,nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def __str__(self):
        return "Nome:{nome}\nIdade:{idade}\nPeso:{peso}\nAltura:{altura:.2f}\n\n"\
        .format(
            nome = self.nome,
            idade = self.idade,
            peso = self.peso,
            altura = self.altura
            )

    def evenelhecer(self, anos=1):
        self.idade += anos

        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, engordar):
        self.peso += engordar

    def emagrecer(self, emagrecer):
        self.peso -= emagrecer

    def crescer(self, cm):
        self.altura += (cm/100)




p = Pessoa('mateus',18, 88, 1.88)
print(p)
p.evenelhecer()
print(p)
p.engordar(3)
print(p)
p.emagrecer(1)
print(p)
p.crescer(3)
print(p)