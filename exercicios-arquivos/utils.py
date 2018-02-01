def transform(size):
    '''
    transforma bytes em megabytes
    '''
    try:
        return size / 1024 / 1024
    except ZeroDivisionError:
        return 0


def media_ocupado(total, itens):
    '''
    retorna media ocupada do espaco
    '''
    try:
        return round(total) / len(itens)
    except ZeroDivisionError:
        return 0

def calc_percent(value, total_fill):
    try:
        return transform((value / round(total_fill)) * 100)
    except ZeroDivisionError:
        return 0