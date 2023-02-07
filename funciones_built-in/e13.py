"""Ejercicio 13 > filter() y reduce()"""
# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares
# de una lista pasada por parámetro con filter
# y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce


def sumaPares(lista):
    return reduce(lambda a, b: a + b, filter(lambda x: x % 2, lista))


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sumaPares(numeros))
