def gerando_chars(string='Mateus'):
    for i in string:
        yield ord(i)


lista_chars = gerando_chars('Ola, eu gostaria de saber quando sera o proximo jogo')
for i in lista_chars:
    print(chr(i)+' = '+str(i))