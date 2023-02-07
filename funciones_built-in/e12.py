"""Ejercicio 12 > set(), sorted()"""
# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente
# y separados por comas.

paises = input("Ingrese los países separados por comas: ")
lst_paises = set(paises.split(","))
lista_final = sorted(list(lst_paises))
print(lista_final)
