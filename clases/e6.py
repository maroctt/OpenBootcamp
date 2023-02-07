"""Ejercicio 6"""
# → En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# • Color
# • Ruedas
# • Puertas
# → Por otro lado crearéis la clase Coche la cual heredará de Vehículo
# y tendrá los siguientes atributos:
# • Velocidad
# • Cilindrada
# → Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.


class Vehiculo:
    _ruedas = 4

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, puertas, velocidad, cilindrada):
        super().__init__(color, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


c1 = Coche("rojo", 5, 120, 16)

print(
    f"Coche 1\n-------------\nRuedas:{c1._ruedas}\nColor:{c1.color}\nPuertas:{c1.puertas}\nVelocidad:{c1.velocidad}\nCilindrada:{c1.cilindrada}"
)
