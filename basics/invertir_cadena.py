def invertir_cadena(cadena):
    """
    Funcion que invierte una cadena de caracteres
    """

    cadena_invertida = ""

    for letra in cadena[::-1]:
        cadena_invertida += letra

    return cadena_invertida