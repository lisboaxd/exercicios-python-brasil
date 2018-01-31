#coding: UTF-8
'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''
sexo = input("Digite o sexo: ")
if sexo == 'M' or sexo == 'm':
    texto = 'Masculino'
elif sexo == 'F' or sexo == 'f':
    texto = 'Feminino'
else:
    texto ='Invalido'
print(texto)