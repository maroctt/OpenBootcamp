"""Ejercicio 10 > Input/Output"""
# Crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo.
# Para ello, tendréis que acceder dos veces al archivo creado.

f = open("ej10.txt", "w")
f.write("Mi primer fichero\n--------------\n")
f.close()

f = open("ej10.txt", "a")
lineas = ["Agregando otro contenido al fichero\n", "Otra linea"]
f.writelines(lineas)
