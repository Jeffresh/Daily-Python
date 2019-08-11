
def mult_list_elements(lista):
    """
    función que devuelve la multiplicacion
    de todos los elementos de una lista
    """

    mult_total = 1
    for elemento in lista:
        mult_total *= elemento

    return mult_total


def sum_list_elements(lista):
    """
    función que devuelve la suma de
    todos los elementos de una lista
    """

    sum_total = 0

    for elemento in lista:
        sum_total += elemento

    return sum_total