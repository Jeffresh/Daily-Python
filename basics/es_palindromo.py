from basics import invertir_cadena as basic


def es_palindromo(cadena):
    """
    Función que comprueba si una cadena es un palindromo
    """
    cadena_invertida = basic.invertir_cadena(cadena)
    iterador = 0
    for letra in cadena_invertida:
        if cadena[iterador] == letra:
            iterador += 1
        else:
            return False

    return True
