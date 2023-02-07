"""Crar tabla Alumnos: 3 columnas, id, nombre, apellido. Insertar 8 registros"""

# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# • id de tipo entero,
# • nombre de tipo texto
# • apellido de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos
# Por último, tienes que realizar una búsqueda de un alumno por nombre
# y mostrar los datos por consola.

import sqlite3


def main():
    """Main app"""
    alumnos = [
        {"ide": 0, "nombre": "Juan", "apellido": "Abc"},
        {"ide": 1, "nombre": "Mari", "apellido": "Def"},
        {"ide": 2, "nombre": "Laiy", "apellido": "Ghi"},
        {"ide": 3, "nombre": "Lola", "apellido": "Jkl"},
        {"ide": 4, "nombre": "Pepito", "apellido": "Mnñ"},
        {"ide": 5, "nombre": "Moritz", "apellido": "Opq"},
        {"ide": 6, "nombre": "Luan", "apellido": "Rst"},
        {"ide": 7, "nombre": "Meiyj", "apellido": "Vwx"},
    ]
    crear_tabla("miapp.db")
    insertar_alumnos(alumnos, "miapp.db")
    buscar_alumno("miapp.db", "Moritz")


def crear_tabla(base_datos):
    """Crear tabla Alumnos"""
    conn = sqlite3.connect(base_datos)
    cur = conn.cursor()

    query = """CREATE TABLE IF NOT EXISTS alumnos(
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL
                );
            """

    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def insertar_alumnos(alumnos, bd):
    """Insertar registros a la tabla alumnos"""
    conn = sqlite3.connect(bd)
    cur = conn.cursor()
    query = """INSERT INTO alumnos(id,nombre,apellido) VALUES(?,?,?)"""
    for alumno in alumnos:
        cur.execute(
            query, (alumno["ide"], alumno["nombre"], alumno["apellido"]))
    conn.commit()
    cur.close()
    conn.close()


def buscar_alumno(bd, nombre):
    """Buscar un alumno por nombre"""
    conn = sqlite3.connect(bd)
    cur = conn.cursor()
    query = f'''SELECT * FROM alumnos WHERE nombre="{nombre}"'''
    rows = cur.execute(query)
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
