#coding:UTF-8
'''
Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''
farenheit = float(input("Insira a temperatura em Fahrenheit: "))
celsius = (5 * (farenheit - 32) / 9)
print("Temperatura: {0:.2f} ºC".format(celsius))
