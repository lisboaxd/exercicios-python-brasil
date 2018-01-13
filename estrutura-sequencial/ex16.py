#coding:UTF-8
'''Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
import math
import os
os.system('clear')
area = int(input('Digite o tamanho da area a ser pintada: '))
litros = area / 3
latas = litros / 18
print("\n\nSerá necessário comprar {latas} latas\nValor Total:R$ {total}".format(
    latas=math.ceil(latas),
    total=round(latas * 80,2)
    )
)
