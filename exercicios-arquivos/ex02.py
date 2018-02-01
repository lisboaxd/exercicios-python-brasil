#condig: UTF-8
import re
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
total_ocupado = "{0:.2f}".format((total_disco/1024)/1024)
for index, user in enumerate(usu):
    percent = str(((user[1] / round(float(total_ocupado)) * 100) / 1024 / 1024))
    dados += "{0}\t{1}\t{2}\t\t{3:.5s}%\n".format(
        index + 1,
        user[0].capitalize()+'\t' if len(user[0]) <= 7 else user[0].capitalize(),
        str(user[1]),
        '\t'+percent if len(str(user[1])) <= 7 else percent
        )

print(texto.format(
    dados=dados,
    total_ocupado=total_ocupado,
    medio_ocupado='{0:.2f}'.format(round(float(total_ocupado)) / len(usu))
    )
)
