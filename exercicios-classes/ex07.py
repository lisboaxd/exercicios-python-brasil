'''Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    Atributos: Nome, Fome, Saúde e Idade b. 
    Métodos: Alterar Nome, Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. '''

class Tamagushi(object):

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome):
        self.nome = nome

    def retornar_nome(self):
        print('Nome: ',self.nome)

    def retornar_fome(self):
        print('Fome: ',self.fome)

    def retornar_saude(self):
        print('Saude: ',self.saude)

    def retornar_idade(self):
        print('Idade: ',self.idade)

    def retornar_humor(self):
        if self.saude >= 75 and self.fome >= 75:
            print('Excelente')
        elif 50 <= self.saude < 75 and 50 <= self.fome < 75:
            print('Bom')
        elif 25 <= self.saude < 50 and 25 <= self.fome < 50:
            print('Normal')
        elif 0 <= self.saude < 25 and 0 <= self.fome < 25:
            print(u'Péssimo')

t = Tamagushi('Lukke', 65, 65, 1)
t.retornar_humor()
t.retornar_nome()
t.alterar_nome('Alberto')
t.retornar_nome()
t.retornar_idade()
t.retornar_fome()
t.retornar_saude()