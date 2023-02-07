"""Ejercicio 9 > utilizar el modulo time"""
# Crear un script que nos diga si es la hora de ir a casa.
# Tendréis que hacer uso del modulo time.
# Necesitaréis la fecha del sistema y poder comprobar la hora.
# En el caso de que sean más de las 7, se mostrará un mensaje
# y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
import time


def comprobar_hora():
    """Función para comprobar si es la hora de ir a casa."""
    min_salida = 19 * 60
    hora_actual = int(time.strftime("%H"))
    min_actual = int(time.strftime("%M"))

    tot_min = hora_actual * 60 + min_actual
    horas_restantes = (min_salida - tot_min) // 60
    min_restantes = (min_salida - tot_min) % 60

    if hora_actual >= 19:
        print("Es hora de ir a casa!")
    else:
        print(
            f"Todavía no es hora de ir a casa. Faltan {horas_restantes}h {min_restantes}m"
        )


comprobar_hora()
