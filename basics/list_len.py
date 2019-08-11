
def list_len(lista):
    """
    Funcion que devuelve longitud de una lista
    """
    len= 0

    if lista:
        for elementos in lista:
            len += 1

    return len

