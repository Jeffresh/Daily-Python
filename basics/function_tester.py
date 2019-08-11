from basics import max_function as basics

# testing max_function

mayor = basics.maximo(10, 2, 4, 5, 6, 7)

print("El mayor de todos los elentos de la lista es:", mayor)

from basics import list_len as basics

# testing list_leng

lista = [x for x in range(0, 10)]

longitud = basics.list_len(lista)

print("La longitud de la lista es: ", longitud)

# testing es_vocal

from basics import es_vocal as basics

caracteres = ['a', 'b', 'f', 'i']

for caracter in caracteres:
    if basics.es_vocal(caracter):
        print("<", caracter, "> Es una vocal")
    else:
        print("<", caracter, "> No es una vocal")

# testing invertir_Cadena
from basics import invertir_cadena as basics

cadena = "Hola mundo"

print(basics.invertir_cadena(cadena))

# testing es_palindromo

from basics import es_palindromo as basics

cadenas = ['lol', 'hoL']
print(basics.es_palindromo(cadenas[0]))
print(basics.es_palindromo(cadenas[1]))

# testing lista_comun

from basics import lista_comun as basics

lista1 = ['uno', 'dos', 'tres', 'cuatro']
lista2 = ['uno', 'venticinco']
lista3 = ['40', '50', '70']

print(basics.lista_comun(lista1, lista3))
print(basics.lista_comun(lista1, lista2))

#testing n_caracteres
from basics import n_caracteres as basics

print(basics.n_caracteres('*', 5))

#testing histograma

from basics import histograma as basics

lista = [5,6,1,3,6,10,5]

basics.histograma(lista)


