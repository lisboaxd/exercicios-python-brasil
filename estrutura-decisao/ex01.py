# coding:UTF-8
'''Faça um Programa que peça dois números e imprima o maior deles.
'''
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
result = n1 if n1 > n2 else  n2
print(result)