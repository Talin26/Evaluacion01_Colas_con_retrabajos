from tkinter import *
import tkinter as tk
import queue
import random
import statistics

# Definimos la clase Persona con su constructor
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.retrabajos = 0

# Definimos la función para atender a una persona
def atender_persona(cola):
    # Sacamos a la primera persona de la cola
    persona = cola.get()
    # Simulamos un proceso de atención de personas en una fila
    atendido_correctamente = random.choice([True, False])
    
    if atendido_correctamente:
        area_texto.insert(tk.END, f"La {persona.nombre} fue atendida correctamente.\n")
    else:
        # Si la persona no fue atendida correctamente, incrementamos su contador de retrabajos
        persona.retrabajos += 1
        area_texto.insert(tk.END,f"La {persona.nombre} no fue atendida correctamente. Regresa a la cola.\n")
        # Ponemos a la persona de nuevo en la cola
        cola.put(persona)

    return atendido_correctamente

def procesar():
    # Creamos una cola vacía
    cola = queue.Queue()
    # Creamos una lista vacía para almacenar los clientes
    personas_array = []
    nro_personas = casilla_personas.get()
    
    minimo = casilla_minimo.get()
    maximo = casilla_maximo.get()
    
    if not nro_personas.isdigit() or int(nro_personas) <= 0 or not minimo.isdigit() or int(minimo) <= 0 or not maximo.isdigit() or int(maximo) <= 0:
        area_texto.delete("1.0", tk.END)
        area_texto.insert(tk.END, "Error: El valor debe ser un numero o en dado caso Debe ingresar un número mayor a 0.\n")
        return
    else:
        nro_personas = int(casilla_personas.get())
        # Creamos n personas segun se digite por el usuario y los añadimos a la lista y a la cola
        for i in range(nro_personas):
            nombre = f"Persona Nro {i+1} en la cola, "
            persona = Persona(nombre)
            personas_array.append(persona)
            cola.put(persona)

        # Creamos una lista vacía para almacenar los tiempos de atención
        lista_tiempos = []
        # Creamos un contador para los retrabajos
        retrabajos = 0
        minimo = int(casilla_minimo.get())
        maximo = int(casilla_maximo.get())
        # Mientras la cola no esté vacía, atendemos a los clientes
        while not cola.empty():
            # Simulamos el tiempo que toma atender a un cliente
            tiempo = random.randint(minimo, maximo)
            # Añadimos el tiempo a la lista de tiempos
            lista_tiempos.append(tiempo)
            # Atendemos al cliente
            if not atender_persona(cola):
                retrabajos += 1
        
        # Calculamos el tiempo promedio en el sistema y la tasa de retrabajos
        casilla_tiempo.delete(0,tk.END)
        casilla_tiempo.insert(tk.END, f"{(statistics.mean(lista_tiempos)):.3f} Minutos por persona")
        casilla_promedio.delete(0, tk.END)
        casilla_promedio.insert(tk.END, f"{(retrabajos / len(personas_array)):.3f}")
        
        #Desabilitamos la posibilidad de edicion de las casillas de los resultados una vez los muestre
        casilla_tiempo.config(state="disabled")
        casilla_promedio.config(state="disabled")
        area_texto.config(state="disabled")
        
    
    


def limpiar():
    casilla_tiempo.config(state="normal")
    casilla_promedio.config(state="normal")
    area_texto.config(state="normal")
    
    area_texto.delete("1.0", tk.END)
    casilla_personas.delete(0, tk.END)
    casilla_promedio.delete(0, tk.END)
    casilla_tiempo.delete(0, tk.END)
    casilla_minimo.delete(0,tk.END)
    casilla_maximo.delete(0,tk.END)
    

Ventana_principal = Tk()
Ventana_principal.title("COLAS CON RETRABAJOS     Stalin Salazar C.I 25107117")
Ventana_principal.resizable(False, False)
Ventana_principal.iconbitmap("iconoStalin.ico")


# Panel principal de la ventana
panel_principal = Frame(Ventana_principal)
panel_principal.configure(width=1200, height=650,background="DeepSkyBlue3", relief="solid", border=5)
panel_principal.pack(fill="both", expand="True")

titulo = Label(panel_principal)
titulo.configure(text="ATENCION AL PUBLICO DE CONSULADO", font=("Arial", 30, "bold"), foreground="black", background="DeepSkyBlue3")
titulo.place(x=200, y=20)

# Panel de Botones e ingreso de datos
frame1 = Frame(panel_principal)
frame1.configure(width=300, height=490, background="khaki",border=5, relief="solid")
frame1.place(x=40, y=100)

# Texto que indica la cantidad de personas que se encuentran en la fila/cola
texto_personas = Label(frame1)
texto_personas.configure(text="Ingrese Nro de Personas \nen cola", font=("Arial", 16, "bold"), foreground="SlateBlue4", background="khaki")
texto_personas.place(x=20, y=50)

#Casilla para digitar la cantidad de personas existentes en la fila/cola
casilla_personas = Entry(frame1)
casilla_personas.configure(font=("Arial", 15), foreground="black", border=5)
casilla_personas.place(x=30, y=110)

#Leyenda que indica donde colocar el intervalo de tiempo que tardan por atender a cada persona
texto_tiempo = Label(frame1)
texto_tiempo.configure(text="Ingrese el intervalo\n promedio de tiempo \nde atención", font=("Arial", 16, "bold"), foreground="SlateBlue4", background="khaki")
texto_tiempo.place(x=35, y=170)

#texto que indica el tiempo minimo que se tarda en atender a una persona (lo minimo es 1 minuto)
texto_minimo = Label(frame1)
texto_minimo.configure(text="Minimo", font=("Arial", 16, "bold"), foreground="SlateBlue4", background="khaki")
texto_minimo.place(x=30, y=260)

#Casilla donde se coloca el tiempo minimo que se tarda en atender a una persona 
casilla_minimo = Entry(frame1)
casilla_minimo.configure(font=("Arial", 15), foreground="black", border=5, width=10)
casilla_minimo.place(x=130, y=260)

#texto que indica el tiempo maximo que se tarda en atender a una persona 
texto_maximo = Label(frame1)
texto_maximo.configure(text="Maximo", font=("Arial", 16, "bold"), foreground="SlateBlue4", background="khaki")
texto_maximo.place(x=30, y=310)

#Casilla donde se coloca el tiempo maximo que se tarda en atender a una persona 
casilla_maximo = Entry(frame1)
casilla_maximo.configure(font=("Arial", 15), foreground="black", border=5, width=10)
casilla_maximo.place(x=130, y=310)

# Area de texto que muestra el proceso de colas con retrabajos
area_texto = Text(Ventana_principal)
area_texto.configure(height=16, width=67, font=("Arial", 14), foreground="black", border=5, relief="solid")
area_texto.place(x=400, y=105)

#Texto que explica el resultado del promedio del tiempo de atencion por persona
texto_tiempo = Label(Ventana_principal)
texto_tiempo.configure(text="Tiempo Promedio", font=("Arial", 16, "bold"), foreground="black", background="DeepSkyBlue3")
texto_tiempo.place(x=400, y=520)

# Casilla donde se muestra el resultado del promedio del tiempo de atencion por persona
casilla_tiempo = Entry(Ventana_principal)
casilla_tiempo.configure(font=("Arial", 15), foreground="black", border=5, width=30)
casilla_tiempo.place(x=400, y=560)

#Texto que explica donde se muestra la taza de retrabajos
texto_promedio = Label(Ventana_principal)
texto_promedio.configure(text="Tasa de Retrabajos", font=("Arial", 16, "bold"), foreground="black", background="DeepSkyBlue3")
texto_promedio.place(x=780, y=520)

#Casilla donde muestra la taza de retrabajos
casilla_promedio = Entry(Ventana_principal)
casilla_promedio.configure(font=("Arial", 15), foreground="black", border=5, width=30)
casilla_promedio.place(x=780, y=560)

# Boton que inicia la simulación
boton_simular = Button(frame1)
boton_simular.configure(text="Procesar", cursor="hand2", font=("Arial", 14), width=8, background="SlateBlue1", command = lambda:procesar())
boton_simular.place(x=30, y=390)

# Boton que borra el contenido de las casillas y del area de texto
boton_borrar = Button(frame1)
boton_borrar.configure(text="Borrar", cursor="hand2", font=("Arial", 14), width=8, background="SlateBlue1", command=limpiar)
boton_borrar.place(x=160, y=390)


Ventana_principal.mainloop()