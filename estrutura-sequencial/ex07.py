#coding: UTF-8
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro \
# desta área para o usuário.
altura = float(input('Digite a Altura do quadrado: '))
comp = float(input('Digite o Comprimento do quadrado: '))
print("A área do quadrado é {0} e seu dobro é {1}".format(altura*comp, 2*(altura*comp)))