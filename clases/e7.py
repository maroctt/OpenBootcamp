"""Ejercicio 7"""
# Tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos>
# • nombre
# • nota
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos
# y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


class Alumno:
    _aprobo = False

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        self.aprobo()

    def aprobo(self):
        if self.nota > 5:
            self._aprobo = True

    def __str__(self):
        return f"{self.nombre} tuvo una nota de: {self.nota}. {'Aprobó la materia' if self._aprobo else 'No aprobó la materia'}"


alu1 = Alumno("Pepito", 6)
print(alu1)

alu2 = Alumno("Juanito", 4)
print(alu2)
