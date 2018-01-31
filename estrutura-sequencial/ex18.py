# coding:UTF-8
'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
tamanho = int(input("Digite o tamanho do arquivo em MB: "))
velocidade = int(input("Qual a velocidade do seu link de Internet em Mbps: "))
tempo = (tamanho / velocidade) / 60
print("Tempo aproximado para concluir o download: {tempo} minuto(s)".format(tempo=tempo))
