def main():
    servicios = listarServicios()
    for servicio in servicios:
        print(f"Servicio: {servicio[0]} | Puerto/Protocolo:{servicio[1]}")


def listarServicios():
    f = open("C:/Windows/System32/drivers/etc/services", "r")
    datos = f.readlines()
    f.close()

    resultado = []

    for linea in datos:
        if linea[0] == "#" or linea[0] == "\n":
            continue

        partes = linea.split()

        resultado.append(partes[0:2])

    return resultado


if __name__ == "__main__":
    main()
