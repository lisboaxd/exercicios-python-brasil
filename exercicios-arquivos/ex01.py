#coding: UTF-8
'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
'''

def check(num):
    if (int(num[0]) >= 1 and int(num[0]) <= 255) and \
    int(num[1]) <= 255 and \
    int(num[2]) <= 255 and \
    int(num[3]) <= 255:
        return True

file = open('lista-ips.txt','r')

cont = file.readlines()
lista = []
invalidos = []
for line in cont:
    octectos = line.rstrip('\n').split('.')
    if check(octectos):
        lista.append('.'.join(octectos))
    else:
        invalidos.append('.'.join(octectos))
file.close()

file = open('ips-validos.txt','w')
file.write("[Endereços válidos:]\n")
for ip in lista:
    file.write(ip+'\n')
file.write("[Endereços inválidos:]\n")
for ip in invalidos:
    file.write(ip+'\n')
file.close()

