def gerando_lista(stop):
    """
    É um generator
    :return: 
    """
    for i in range(stop):
        yield  i


a = gerando_lista(10)
print(a)
3 in a