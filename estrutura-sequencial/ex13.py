#Tendo como dados de entrada a altura e o sexo de uma pessoa,
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo
def calculapeso(sexo,altura,peso):
    p = int((62.1 * altura) - 44.7) if sexo != 's' else int((72.7*altura) - 58)
    peso = int(peso)
    resp = 'Peso ideal' if p == peso else 'Acima do peso, seu peso ideal e: {0:.2f}'.format(p)
    resp = "Abaixo do peso, seu peso ideal e: {0:.2f}".format(p) if peso < p else resp
    return resp

altura = float(input("Insira sua altura: "))
sexo = input(u"Voce e homem? s (SIM) qualquer tecla (NAO): ")
peso_p = float(input('Qual seu peso? (K.g): '))

print(calculapeso(sexo,altura,peso_p))