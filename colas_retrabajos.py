from tkinter import *
import tkinter as tk

Ventana_principal = Tk()
Ventana_principal.title("COLAS CON RETRABAJOS")
Ventana_principal.resizable(False, False)
Ventana_principal.iconbitmap("iconoStalin.ico")
#Ventana_principal.attributes("-alpha",1)

#Panel principal de la ventana
panel_principal = Frame(Ventana_principal)
panel_principal.configure(width=1100, height=650, background="SteelBlue2",relief="solid", border=5)
panel_principal.pack(fill="both", expand="True")

#Panel de Botones e ingreso de datos
frame1 = Frame(panel_principal)
frame1.configure(width=300, height=550, background="khaki", border=5, relief="solid")
frame1.place(x=40, y=40)

#Texto que indica la cantidad de personas que se encuentran en la fila/cola
texto_personas = Label(frame1)
texto_personas.configure(text="Nro de Personas", font=("Arial", 16, "bold"), foreground="black", background="khaki")
texto_personas.place(x=60, y=180)

#Casilla para digitar la cantidad de personas existentes en la fila/cola
casilla_personas = Entry(frame1)
casilla_personas.configure(font=("Arial", 15), foreground="black", border=5)
casilla_personas.place(x=30, y=230)

#Boton que inicia la simulación
boton_simular = Button(frame1)
boton_simular.configure(text="Procesar",cursor="hand2", font=("Arial", 14), width=8, background="SlateBlue1")
boton_simular.place(x=30, y=300)

#Boton que borra el contenido de las casillas y del area de texto
boton_borrar = Button(frame1)
boton_borrar.configure(text="Borrar",cursor="hand2", font=("Arial", 14), width=8, background="SlateBlue1")
boton_borrar.place(x=160, y=300)

#Area de texto que muestra el proceso de colas con retrabajos
area_texto = Text(Ventana_principal)
area_texto.configure(height=20, width=57, font=("Arial", 14), foreground="black", border=5, relief="solid")
area_texto.place(x=400, y=45)

texto_tiempo = Label(Ventana_principal)
texto_tiempo.configure(text="Tiempo Promedio", font=("Arial", 16, "bold"), foreground="black", background="SteelBlue2")
texto_tiempo.place(x=400, y=520)

casilla_tiempo = Entry(Ventana_principal)
casilla_tiempo.configure(font=("Arial", 15), foreground="black", border=5, width=25)
casilla_tiempo.place(x=400, y=560)

texto_promedio = Label(Ventana_principal)
texto_promedio.configure(text="Tasa de Retrabajos", font=("Arial", 16, "bold"), foreground="black", background="SteelBlue2")
texto_promedio.place(x=750, y=520)

casilla_promedio = Entry(Ventana_principal)
casilla_promedio.configure(font=("Arial", 15), foreground="black", border=5, width=25)
casilla_promedio.place(x=750, y=560)


Ventana_principal.mainloop()