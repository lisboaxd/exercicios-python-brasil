#condig: UTF-8
import re
from utils import transform, media_ocupado, calc_percent
usu = []
total_disco = 0
with open('usuarios.txt','r') as a:
    usuarios = a.readlines()
    for u in usuarios:
        usuario, espaco = re.sub(r"[ ]+","#",u.rstrip("\n")).split("#")
        usu.append([usuario, int(espaco)])
        total_disco += int(espaco)
    a.close()

texto = \
'''
ACME Inc.\t\tUso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.\tUsuário\t\tEspaço utilizado\t% do uso
{dados}
Espaço total ocupado: {total_ocupado} MB
Espaço médio ocupado: {medio_ocupado} MB
'''
dados = ''
total_ocupado = transform(total_disco)
for index, user in enumerate(usu):
    percent = str(calc_percent(user[1], total_ocupado))
    dados += "{0}\t{1}\t{2}\t\t{3:.5s}%\n".format(
        index + 1,
        user[0].capitalize()+'\t' if len(user[0]) <= 7 else user[0].capitalize(),
        str(user[1]),
        '\t'+percent if len(str(user[1])) <= 7 else percent
        )

texto = texto.format(
    dados=dados,
    total_ocupado='{0:.2f}'.format(total_ocupado),
    medio_ocupado='{0:.2f}'.format(media_ocupado(total_ocupado, usu))
    )


with open('relatorio.txt','w') as relatorio:
    relatorio.writelines(texto)
    print("Processo concluido, verifiqueo arquivo {0}".format(relatorio.name))
