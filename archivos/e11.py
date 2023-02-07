"""Ejercicio 11 > Input/Output"""
# Crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella,
# lo guardaréis en un archivo y luego lo cargamos.
import pickle

FICHERO = "datos.bin"


class Vehiculo:
    """Clase para representar un vehículo"""

    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas


def main():
    """Aplicación principal"""
    print("Guardando los datos del objeto...")
    guardar_datos()
    print(f"Datos guardados en {FICHERO}")
    print(f"Cargando los datos de {FICHERO}...")
    cargar_datos()


def guardar_datos():
    """Función para guardar los datos en el fichero"""
    v1 = Vehiculo("azul", 5)
    f = open(FICHERO, "wb")
    pickle.dump(v1, f)
    f.close()


def cargar_datos():
    """Función para cargar los datos del fichero"""
    f = open(FICHERO, "rb")
    v1 = pickle.load(f)
    f.close()
    print(f"Vehiculo 1\nColor:{v1.color}\nPuertas:{v1.puertas}")


if __name__ == "__main__":
    main()
