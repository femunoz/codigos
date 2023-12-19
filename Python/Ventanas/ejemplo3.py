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

# 4 componentes (widgets):
'''
1. Ventana
2. 1 Label
3. 1 Entry
4. 1 Label
'''

def saludar(x): # vamos a la documentación de bind de clase Button.
    r = campo_texto.get() # respuesta del campo de texto
    # actualizamos el texto del Label hola 
    hola.config(text="hola "+r)  

vent = Tk()

hola = Label(vent, text="hola Juanito")
pregunta = Label(vent, text="Cuál estu nombre?")
campo_texto = Entry(vent) # recibe como param. sólo su contenedor

# ahora haremos los pack de cada widget.
# el orden en que se escribe van del wiget superior
# al widget que va al final de la ventana.

pregunta.pack()
campo_texto.pack()
hola.pack()

# sólo nos falta RELACIONAR o CONECTAR (bind)  el campo de texto
# y la acción que se realizará al presionar <Enter>.

campo_texto.bind("<Return>",saludar)
# IMPORTANTE: No olvidar los caracteres "<" y ">" para el 1er parám.


vent.mainloop()

#veamos qué pasó
# Estos son los ejemplos que vimos en esta sesión. 
# Les invito a revisar y resolver los demás del apunte.

#Gracias por su atención! =)

