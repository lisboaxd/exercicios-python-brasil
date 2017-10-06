#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from  math import pi
raio = float(input(u"Insira o raio do círculo: "))
area = pi*(raio**2)
print("A área do cícurlo é : {0}".format(area))
