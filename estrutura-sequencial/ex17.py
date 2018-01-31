'''Faça um Programa para uma loja de tintas. O programa deverá pedir 
o tamanho em metros quadrados da área a ser pintada. Considere que a
cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga 
e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
from math import ceil
area = int(input('Area em metros quadrados: '))
litros = area / 6
mix = litros / 18 + 3.6 if litros % 18 <= 3.6 else  litros / 18
texto = '''    Você irá gastar {litros} litros para pintar a area de {area} metros:
    Podendo ser {grande:.0f} latas de 18 litros, custando R${grande_preco:.2f}
    Ou {pequena:.0f} latas de 3.6 litros, custando R${pequena_preco:.2f}
    OU {mix:.0f} latas de tinta, sendo uma de 3.6 litros, custando R${mix_preco:.2f}
'''.format(
    litros=litros, 
    area = area, 
    grande = ceil(litros / 18), 
    grande_preco = ceil(litros / 18) * 80,
    pequena = ceil(litros / 3.6),
    pequena_preco = ceil(litros / 3.6) * 25,
    mix= ceil(mix),
    mix_preco = 80 * (mix - 1) + 25
    )
print(texto)