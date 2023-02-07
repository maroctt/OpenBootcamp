"""Ejercicio 15"""
# crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

import tkinter as tk
from tkinter import ttk

wd = tk.Tk()
wd.columnconfigure(0, weight=1)
wd.columnconfigure(1, weight=3)


def aceptar():
    label_aceptar.config(
        text=f"Lenguaje seleccionado:{lenguajes.get(lenguajes.curselection())}"
    )


def salir():
    wd.quit()


label = ttk.Label(
    wd,
    text="Seleccione un lenguaje de programación",
    background="black",
    foreground="white",
)
label.grid(column=0, row=0, ipadx=10, ipady=10, columnspan=3)

label_aceptar = ttk.Label(wd, text="")
label_aceptar.grid(column=0, row=1)

lista = ["Python", "C#", "Java", ".NET", "JavaScript", "Go"]
lista_items = tk.StringVar(value=lista)
lenguajes = tk.Listbox(wd, listvariable=lista_items)
lenguajes.grid(column=0, row=2, columnspan=2)

btn_aceptar = ttk.Button(wd, text="Aceptar", command=aceptar)
btn_salir = ttk.Button(wd, text="Salir", command=salir)
btn_aceptar.grid(column=1, row=3)
btn_salir.grid(column=0, row=3)
wd.mainloop()
