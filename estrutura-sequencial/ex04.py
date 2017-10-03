#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
lista = []
i = 0
while len(lista) < 4:
    i = i + 1
    lista.append(int(input('Insira a nota {}: '.format(i))))

print((sum(lista))/len(lista))