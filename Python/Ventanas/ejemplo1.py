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

# más detalles de tkinter en su documentación

ventana = Tk()

# el "Hola" que se ve en a ventana corresponde a una
# etiqueta: clase Label en tkinter

saludo = Label(ventana, text = "Hola")

# la ventana es el contenedor principal.
# corresponde a un objeto
# este lo guardamos en la referencia "ventana" (linea 17)

# al crear un label debemos primero especificar su contenedor.

# como podemos ver en la documentación de la web anterior,
# la interfaz tkinter "Describes the Tkinter widget set for 
# constructing graphical user interfaces (GUIs) in the Python 
# programming language. Includes coverage of the ttk themed 
# widgets."

# widget: cualquier elemento de la interfaz tkinter:
# Labels, Buttons y más.

# en esta documentación podemos confirmar lo especificado previa-
# mente.
# el objeto "ventana" es un contenedor y es el primer
# parámetro del constructor Label.
# los siguientes son opciones.

# la opción text fue la que usamos al INSTANCIAR o crear
# un objeto de tipo Label (línea 22).
# IMPORTANTE: DEBE especificarse la opción a utilizar: "text"

# Una vez creado este widget Label, lo acomodamos dentro de la
# ventana:

saludo.pack()

# Finalmente, en toda ventana DEBE haber una línea con un 
# un mainloop:

ventana.mainloop()

