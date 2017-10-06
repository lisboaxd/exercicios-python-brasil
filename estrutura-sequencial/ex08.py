#coding:UTF-8
'''Faça um Programa que pergunte quanto você ganha por hora e o número
de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
valor_hr= float(input(u"Quanto você ganha por hora? "))
num_hr = int(input(u"Quantas horas vocẽ trabalha por mês? "))
print("{0:.2f}".format(valor_hr*num_hr))