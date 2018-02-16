'''Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. '''


class Tv(object):

    def __init__(self, polegadas, cor, modelo):
        self.polegadas = polegadas
        self.cor = cor
        self.modelo = modelo
        self.volume = 10
        self.canal = 12
        self.error = ''

    def __str__(self):
        return "Canal:{canal}\nVolume:{volume}\nMensagem:{erro}\n\n"\
        .format(
            canal = self.canal,
            volume = self.volume,
            erro = self.error
            )

    def mudar_canal(self, canal):
        if canal > 0 and canal < 100:
            self.canal = canal
            self.error = ''
        else:
            self.error = 'Esse canal está fora da Faixa de Canais'
    

    def subir_canal(self):
        if self.canal <= 100 and self.canal > 0:
            self.canal += 1
    
    def descer_canal(self):
        if self.canal <= 100 and self.canal > 1:
            self.canal -= 1

    def aumentar_vol(self):
        if self.volume >= 0 and self.volume <= 100:
            self.volume += 1

    def diminuir_vol(self):
        if self.volume >= 0 and self.volume <= 100:
            self.volume -= 1

tv = Tv(44,'preta','LCD')
print(tv)
tv.subir_canal()
tv.aumentar_vol()
tv.aumentar_vol()
tv.aumentar_vol()
tv.aumentar_vol()
print(tv)
tv.diminuir_vol()
tv.subir_canal()
print(tv)
tv.descer_canal()
print(tv)
tv.mudar_canal(150)
print(tv)
tv.mudar_canal(56)
print(tv)