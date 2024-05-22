# Apuntes del profesor
# Juán Alvarez
# DCC, UChile.

# Módulo Tkinter:
# creación de ventanas en Python

# las siguientes dos líneas SIEMPRE
# las utilizaremos para crear ventanas en Python
# esto con el módulo tkinter.

from tkinter import *
from tkinter import ttk

# 4 widgets: ventana, 2 botones y 1 Label

# IMPORTANTE: Al haber un botón, este debe realizar 
# una acción al momento de que recibe un click.
# Primero construiremos la ventana de este ejemplo y luego
# abordaremos lo denominado EVENTOS

def saludar():
    saludo.config(text="hola")
def greet():
    saludo.config(text="hello")


vent = Tk()
# nuevamente su contenedor es vent
# veamos qué opciones ofrece...
boton1 = Button(vent, text="español", command=saludar)

boton1.pack()

# OJO! Intencionalmente no usaremos el 3er. parámetro,
# para ver qué pasa...
# Nada ocurrió. No especificamos el 3er parámetro "command"


boton2 = Button(vent, text="english" , command=greet)
boton2.pack()
saludo = Label(vent)

saludo.pack()
# debemos hacerlo con cada widget...

vent.mainloop()