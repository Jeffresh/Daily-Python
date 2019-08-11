def lista_comun(lista1,lista2):

    for elemento in lista1:
        if elemento in lista2:
            return True

    return False


