# coding: UTF-8
'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
letra = input("Digite uma letra: ")
if letra.isalpha():
    if letra in ['a','e','i','o','u']:
        print('vogal')
    else:
        print('consoante')
else:
    print("Digite apenas letras")