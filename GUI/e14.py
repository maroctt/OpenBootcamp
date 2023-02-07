""" Ejercicio 14 """
# En este ejercicio tenéis que crear una lista de RadioButton que muestre
# la opción que se ha seleccionado y que contenga un botón de reinicio
# para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.

import tkinter as tk
from tkinter import ttk, StringVar

wd = tk.Tk()


def update_label():
    label_seleccion.config(text=seleccionado.get())


def reset():
    seleccionado.set(None)
    label_seleccion.config(text="")


wd.columnconfigure(0, weight=1)
wd.columnconfigure(1, weight=3)

seleccionado = tk.StringVar()
seleccionado.set(None)

r1 = ttk.Radiobutton(
    wd, text="Python", value="Python", variable=seleccionado, command=update_label
)
r2 = ttk.Radiobutton(
    wd, text="C#", value="C#", variable=seleccionado, command=update_label
)
r3 = ttk.Radiobutton(
    wd, text=".NET", value=".NET", variable=seleccionado, command=update_label
)
r4 = ttk.Radiobutton(
    wd, text="Java", value="Java", variable=seleccionado, command=update_label
)

label_seleccion = ttk.Label(wd, text="")

btn_reset = ttk.Button(wd, text="Reset", command=reset)

r1.grid(column=0, row=1)
r2.grid(column=0, row=2)
r3.grid(column=0, row=3)
r4.grid(column=0, row=4)
label_seleccion.grid(column=0, row=0, padx=5, pady=5)
btn_reset.grid(column=1, row=5)


wd.mainloop()
