"""M[odulo para el ejercicio 8"""
# Crear un módulo que contenga las operaciones básicas de una calculadora:
# → sumar, restar, multiplicar y dividir.
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
# Los resultados tenéis que mostrarlos por consola.


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: división por cero."
    else:
        return a / b
