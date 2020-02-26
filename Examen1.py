import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

# Funciones para ventanas emergentes
def funcion_box1(x):
    mBox.showinfo('Tus Datos son: ',x)

def funcion_box2():
    mBox.showinfo('Error','Espacios incompletos')

# Funciones de validacion para la captura de datos pestañas 1 y 2
def funcion_validarp1():
    for i in Lista:
        if not i: 
            return False
    return True

def funcion_validarp2():
    if sctext.get(1.0, tk.END) == "\n":
        return False
    return True

# Funcion Captura Pestaña 2
def funcion_capture2():
    Lista2.clear()
    if funcion_validarp2() == False:
        funcion_box2()
        return
    texto = "Pasatiempos: "
    if Check.get() == 1: Lista2.append("Leer")
    if Check2.get() == 1: Lista2.append("Peliculas")
    if Check3.get() == 1: Lista2.append("Redes sociales")
    
    for i in Lista2:
        texto+=i+", "
    texto+="\n"+"Estado: "
    if Opcion.get() == 1: texto+="Soltero"
    if Opcion.get() == 2: texto+="Casado"
    if Opcion.get() == 3: texto+="Viudo"
    texto+="\n"+"Objetivo de la vida: "+"\n"+sctext.get(1.0, tk.END)
    funcion_box1(texto)

# Funcion Captura Pestaña 1
def funcion_capture():
    Lista.clear()
    Lista.append(nombre.get())
    Lista.append(apellidoPaterno.get())
    Lista.append(apellidoMaterno.get())
    Lista.append(direccion.get())
    Lista.append(colonia.get())
    Lista.append(ciudad.get())
    Lista.append(municipio.get())
    if funcion_validarp1() == False:
        funcion_box2()
        return
    x =  ""
    y = 0
    for i in Lista:
        if(y == 0):
            x+="Nombre: "+i+"\n"
        if(y == 1):
            x+="Apellido Paterno: "+i+"\n"
        if(y == 2):
            x+="Apellido Materno: "+i+"\n"
        if(y == 3):
            x+="Direccion: "+i+"\n"
        if(y == 4):
            x+="Colonia: "+i+"\n"
        if(y == 5):
            x+="Ciudad: "+i+"\n"
        if(y == 6):
            x+="Municipio: "+i
        y+=1
    funcion_box1(x)
    
# Funcion captura del menu imprimir
def funcion_capture3():
    Lista.clear()
    Lista.append(nombre.get())
    Lista.append(apellidoPaterno.get())
    Lista.append(apellidoMaterno.get())
    Lista.append(direccion.get())
    Lista.append(colonia.get())
    Lista.append(ciudad.get())
    Lista.append(municipio.get())
    if funcion_validarp1() == False:
        funcion_box2()
        return
    x =  ""
    y = 0
    for i in Lista:
        if(y == 0):
            x+="Nombre: "+i+"\n"
        if(y == 1):
            x+="Apellido Paterno: "+i+"\n"
        if(y == 2):
            x+="Apellido Materno: "+i+"\n"
        if(y == 3):
            x+="Direccion: "+i+"\n"
        if(y == 4):
            x+="Colonia: "+i+"\n"
        if(y == 5):
            x+="Ciudad: "+i+"\n"
        if(y == 6):
            x+="Municipio: "+i
        y+=1
    Lista2.clear()
    if funcion_validarp2() == False:
        funcion_box2()
        return
    x += "\n"+"Pasatiempos: "
    if Check.get() == 1: Lista2.append("Leer")
    if Check2.get() == 1: Lista2.append("Peliculas")
    if Check3.get() == 1: Lista2.append("Redes sociales")
    
    for i in Lista2:
        x+=i+", "
    x+="\n"+"Estado: "
    if Opcion.get() == 1: x+="Soltero"
    if Opcion.get() == 2: x+="Casado"
    if Opcion.get() == 3: x+="Viudo"
    x+="\n"+"Objetivo de la vida: "+"\n"+sctext.get(1.0, tk.END)
    funcion_box1(x)

ColumnaPestaña1=0
FilaPestaña1=0

ColumnaPestaña2=0
FilaPestaña2=0

def Next():
    global ColumnaPestaña1
    global FilaPestaña1
    ColumnaPestaña1 = 0
    FilaPestaña1 += 1

def Next2():
    global ColumnaPestaña2
    global FilaPestaña2
    ColumnaPestaña2 = 0
    FilaPestaña2 += 1

    
def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()

# Estructura general de la ventana

ventana = tk.Tk()
ventana.title("Examen")

#Lista de Apoyo

Lista = []
Lista2 = []

# Atributos de Pestaña 1

labelPregunta1 = ttk.Label(ventana, text = "Cual es el verbo to be de I?: ")
labelPregunta1.grid(column = ColumnaPestaña1, row = FilaPestaña1)

res1 = tk.StringVar()
ColumnaPestaña1+=1

res1Capturada = ttk.Entry(ventana, width = 20, textvariable = res1)
res1Capturada.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan = 8)
Next()

labelPregunta2 = ttk.Label(ventana, text = "Cual es el pasado de do?: ")
labelPregunta2.grid(column = ColumnaPestaña1, row = FilaPestaña1)

res2 = tk.StringVar()
ColumnaPestaña1+=1

res2Capturada = ttk.Entry(ventana, width = 20, textvariable = res2)
res2Capturada.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan = 8)
Next()

labelPregunta3 = ttk.Label(ventana, text = "Cual de estos verbos esta en pasado?: ")
labelPregunta3.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan = 10)
Next()

res3 = tk.IntVar()
Pregunta3Radio1 = tk.Radiobutton(ventana, text = "Swim", variable = res3, value = 1)
Pregunta3Radio1.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.W)
ColumnaPestaña1 += 1
Pregunta3Radio1.select()

Pregunta3Radio2 = tk.Radiobutton(ventana, text = "Played", variable = res3, value = 2)
Pregunta3Radio2.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.W)
ColumnaPestaña1 += 1

Pregunta3Radio3 = tk.Radiobutton(ventana, text = "Sleep", variable = res3, value = 3)
Pregunta3Radio3.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.E)
Next()

labelPregunta4 = ttk.Label(ventana, text = "Cual de estos verbos es regular?: ")
labelPregunta4.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan = 10)
Next()

res4 = tk.IntVar()
Pregunta4Radio1 = tk.Radiobutton(ventana, text = "Bake", variable = res4, value = 1)
Pregunta4Radio1.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.W)
ColumnaPestaña1 += 1
Pregunta4Radio1.select()

Pregunta4Radio2 = tk.Radiobutton(ventana, text = "Steal", variable = res4, value = 2)
Pregunta4Radio2.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.W)
ColumnaPestaña1 += 1

Pregunta4Radio3 = tk.Radiobutton(ventana, text = "Work", variable = res4, value = 3)
Pregunta4Radio3.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.E)
Next()

labelPregunta5 = ttk.Label(ventana, text = "Cuales de estas es WH questions?")
labelPregunta5.grid(column = ColumnaPestaña1, row = FilaPestaña1, columnspan =10)
Next()

Check = tk.IntVar()
Casilla1 = tk.Checkbutton(ventana, text = "Where", variable = Check)
Casilla1.deselect()
Casilla1.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.W)
ColumnaPestaña1 += 1

Check2 = tk.IntVar()
Casilla2 = tk.Checkbutton(ventana, text = "Do", variable = Check2)
Casilla2.deselect()
Casilla2.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.W)
ColumnaPestaña1 += 1

Check3 = tk.IntVar()
Casilla3 = tk.Checkbutton(ventana, text = "Are", variable = Check3)
Casilla3.deselect()
Casilla3.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.E)
ColumnaPestaña1 += 1

Check3 = tk.IntVar()
Casilla3 = tk.Checkbutton(ventana, text = "What", variable = Check3)
Casilla3.deselect()
Casilla3.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.E)
ColumnaPestaña1 += 1

Check3 = tk.IntVar()
Casilla3 = tk.Checkbutton(ventana, text = "Could", variable = Check3)
Casilla3.deselect()
Casilla3.grid(column = ColumnaPestaña1, row = FilaPestaña1, sticky = tk.E)
Next()

Button = ttk.Button(ventana, text="Boton Imprimir Datos", command = funcion_capture)
Button.grid(column = ColumnaPestaña1, row = FilaPestaña1)



ventana.mainloop()