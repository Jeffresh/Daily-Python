# Definir una función en python que reciba argumentos de tipo numérico y devuelva
# el mayor de ellos.

def maximo(*args):
    """
    Funcion que recibe un número indeterminado de argumentos numéricos
    y devuelve el máximo de ellos.
    """
    m = args[0]
    for numero in args[1:]:
        if numero > m:
            m = numero
    return m

#
# maximo = max(10, 2, 4, 5, 6, 7)
#
# print(maximo)
