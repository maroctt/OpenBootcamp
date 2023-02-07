"""Bases de datos"""
import getpass
import sqlite3


def main2():
    """ Crear usuario"""
    crear_usuario(7, "laiy", "clave7")


def main():
    """Loggearse"""
    username = input("Nombre usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")


def verifica_credenciales(username, password):
    """Funcion de verificacion de usuario"""
    conn = sqlite3.connect("miaplicacion.db")
    cur = conn.cursor()

    query = (
        f'SELECT id FROM users WHERE username="{username}" AND password="{password}"'
    )
    print("Query a ejecutar: ", query)

    rows = cur.execute(query)
    data = rows.fetchone()

    cur.close()
    conn.close()

    return data is not None


def crear_usuario(identificador, usuario, clave):
    """Funcion para crear usuario e insertarlo en la bd"""
    # Puedo poner ',isolation_level=None' para no tener que usar commit()
    conn = sqlite3.connect("miaplicacion.db")
    cur = conn.cursor()

    query = """ INSERT INTO users(id, username, password) VALUES(?,?,?) """
    print("Query a ejecutar: ", query)

    rows = cur.execute(query, ((identificador, usuario, clave)))
    print(type(rows))

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
