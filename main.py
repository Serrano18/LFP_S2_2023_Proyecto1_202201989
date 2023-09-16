from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import json
from tkinter import Text, Scrollbar, filedialog
import math

from palabra import *
from operaciones_un_valor import * 
from operaciones import *

#declaracion de las distintas listas
global numero_fila
global numero_columna
global instruccion
global lista_palabras
global lista_errores
#estas son todas mis palabras validas es el lexico que usare
palabras= [
    'operaciones', 'operacion', 'valor1', 'valor2',
    'suma', 'resta', 'multiplicacion', 'division', 'raiz', 'inverso',
    'seno', 'coseno', 'tangente', 'mod',
    'configuraciones', 'texto', 'fondo', 'fuente', 'forma',
    ':', '[', '{', ',', '}', ']', '.'
]
numero_fila=1
numero_columna=1
lista_palabras=[]
instruccion=[]
lista_errores=[]
def analizador(secuencia):
    global numero_fila
    global numero_columna
    global lista_palabras
    palabra=''
    posicion=0
    while secuencia:
        num=secuencia[posicion]
        posicion +=1
        if num == '\"':
            palabra,secuencia= crear_palabra(secuencia[posicion:])
            if palabra and secuencia:
                numero_columna+=1
                p= Palabra(palabra,numero_fila,numero_columna)    
                lista_palabras.append(p)
                numero_columna+=len(palabra)+1
                posicion=0
        elif num.isdigit():
            token,secuencia = crear_numero(secuencia)
            if token and secuencia:
                numero_columna+=1
                p=Palabra(token,numero_fila,numero_columna)
                lista_palabras.append(p)
                numero_columna+=len(str(token))+1
                posicion=0

        elif num == '[' or num == ']':
            p=Palabra(num,numero_fila,numero_columna)
            lista_palabras.append(p)
            secuencia=secuencia[1:]
            posicion=0
            numero_columna+=1
            
        #por si el texto trae saltos de lineas tabulaciones para que no falle la aplicacion
        elif num == '\n':                       
            secuencia = secuencia[1:]
            posicion=0
            numero_columna =1
            numero_fila+=1
        elif num == '\t':
            numero_columna+=4
            secuencia=secuencia[4:]
            posicion=0
        else:
            secuencia=secuencia[1:]
            posicion = 0
            numero_columna=1

def crear_palabra(secuencia):
    global numero_fila
    global numero_columna
    global lista_palabras
    global lista_errores
    palabra=''
    posicion=''
    for num in secuencia:
        posicion+=num
        if num == '\"':
            return palabra, secuencia[len(posicion):]
        else:
            if num=='@' or num=='!' or num=='|' or num=='#' or num == '$' or num == '%' or num == '&' or num == '(' or num == ')' or num == '=' or num == '?' or num == '¿' or num=='+' or num=='-' or num=='/'or num=='*'or num =='_' or num=='¡'or num=='-' or num==';' or num=='^' or num== 'ª' or num=='º' or num=='€' or num=='½'or num=='~' or num=='°' or num=='©'or num=='·':
                    e=(Palabra(num,numero_fila,numero_columna))
                    lista_errores.append(e)
                    print(num)
            palabra+=num
    return None,None

def crear_numero(secuencia):
    valornume=''
    posicion=''
    decimal=False
    for num in secuencia:
        posicion+=num
        if num == '.':
            decimal=True
        if num == "," or num=='"' or num == ' ' or num=='\n' or num== '\t' or num=='}'or num==']':
            if decimal:
                return float(valornume),secuencia[len(posicion)-1:]#Python usa índices basados en cero, entonces necesito el último carácter procesado.
            else:
                return int(valornume),secuencia[len(posicion)-1:]
        else:
            if num=='@' or num=='!' or num=='|' or num=='#' or num == '$' or num == '%' or num == '&' or num == '(' or num == ')' or num == '=' or num == '?' or num == '¿' or num=='+' or num=='-' or num=='/'or num=='*'or num =='_' or num=='¡'or num=='-' or num==';' or num=='^' or num== 'ª' or num=='º' or num=='€' or num=='½'or num=='~' or num=='°' or num=='©'or num=='·':
                    e=(Palabra(num,numero_fila,numero_columna))
                    print (num)
                    lista_errores.append(e)
            valornume+=num
    return None,None

def operar():
    global instruccion
    global lista_palabras
    operacion = ''
    num1=''
    num2=''
    lista_palabras
    while lista_palabras:
        palabra = lista_palabras.pop(0)
        if palabra.operar(None)=='operaciones':
            operaciones=lista_palabras.pop(0)
        elif palabra.operar(None)=='operacion':
            operacion=lista_palabras.pop(0)
        elif palabra.operar(None)=='valor1':
            num1=lista_palabras.pop(0)
            if num1.operar(None)=='[':
                num1=operar()
        elif palabra.operar(None)=='valor2':
            num2=lista_palabras.pop(0)
            if num2.operar(None)=='[':
                num2=operar()
        
        if operacion and num1 and num2:
            return (Operaciones(num1,num2,operacion,f'{operacion.getFila()}:{operacion.getColumna()}',f':{num2.getFila()}:{num2.getColumna()}'))
        if operacion and num1 and operacion.operar(None)==('seno'or'coseno'or'tangente'):
            return (Operaciones_un_valor(num1,operacion,f'{operacion.getFila()}:{operacion.getColumna()}',f':{num1.getFila()}:{num1.getColumna()}'))

def funcionan():
    global instruccion
    resultado=[]
    while True:
        operacion=operar()
        if operacion:
            resultado.append(f"{operacion.tipo.operar(None)}: {operacion.operar(None)}")
            instruccion.append(operacion)
        else:
            break

    for instruc in instruccion:
        instruc.operar(None)

    textae.delete(1.0, tk.END)  # Borrar el contenido actual de textae
    for res in resultado:
        textae.insert(tk.END, res + '\n')


#ANALIZADOR LEXICO    
def boton_analiza():
    contenido = text.get(1.0, tk.END)
    analizador(contenido)
    funcionan()
    

def boton_error():
    pass


def boton_report():
    pass


#ARCHIVOS
def boton_abre():
    global archivo_actual
    archivo = filedialog.askopenfile(filetypes=[("JSON Files", "*.json")])
    if archivo:
        archivo_actual = archivo.name#almacenamos el noombre
        contenido = json.load(archivo)
        text.delete(1.0, tk.END)  # Borrar el contenido actual del Text
        text.insert(tk.END, json.dumps(contenido, indent=4))

# Función para guardar el contenido actual en un archivo JSON
def boton_guarda():
    global archivo_actual
    if archivo_actual:
        contenido = text.get(1.0, tk.END)
        with open(archivo_actual, 'w') as archivo:
            archivo.write(contenido)

# Función para guardar el contenido actual en un nuevo archivo JSON
def boton_guardac():
    contenido = text.get(1.0, tk.END)
    archivo = filedialog.asksaveasfile(filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    if archivo:
        archivo.write(contenido)

def boton_exit():
    ventana.quit()




#Vista
ventana=tk.Tk()
ventana.title("Analizador Lexico")
ventana.geometry('1024x768')
fuente=tkFont.Font(family='Helvetica', size=13)
ventana.configure(bg='saddle brown')
etiqueta = tk.Label(ventana, bg='saddle brown')
etiqueta.pack(fill=tk.X)
contenedor_botones=tk.Frame(etiqueta,bg='saddle brown')
# Agregar el contenedor de botones a la etiqueta
contenedor_botones.pack(expand=True)
# Crear botones y agregarlos al Frame
boton_analizar = tk.Button(contenedor_botones, text="Analizar",font=fuente ,command=boton_analiza,background="pink")
boton_analizar.grid(row=0, column=0, ipadx=30, ipady=5,padx=50, pady=10)
boton_errores = tk.Button(contenedor_botones, text="Errores", font=fuente ,command=boton_error,background="pink")
boton_errores.grid(row=0, column=1, ipadx=30, ipady=5,padx=50, pady=10)
boton_reporte = tk.Button(contenedor_botones, text="Reporte", font=fuente ,command=boton_report,background="pink")
boton_reporte.grid(row=0, column=2, ipadx=30, ipady=5,padx=50, pady=10)
# Centrar el Frame en la ventana

etiqueta1=tk.Label(ventana,bg='saddle brown')
etiqueta1.pack(side=tk.LEFT,fill=tk.Y,ipadx=5)
contenedor_botones_archivo=tk.Frame(etiqueta1,bg='saddle brown')
# Agregar el contenedor de botones a la etiqueta
contenedor_botones_archivo.pack(ipadx=5,expand=True)
# Crear botones y agregarlos al Frame
boton_abrir = tk.Button(contenedor_botones_archivo, text="Abrir", command=boton_abre,font=fuente,background="pink" )
boton_abrir.pack(ipadx=60, ipady=5,pady=25)
boton_guardar = tk.Button(contenedor_botones_archivo, text="Guardar", command=boton_guarda,font=fuente,background="pink" )
boton_guardar.pack(ipadx=50, ipady=5,pady=25)
boton_guardar_como = tk.Button(contenedor_botones_archivo, text="Guardar Como", command=boton_guardac,font=fuente,background="pink" )
boton_guardar_como.pack(ipadx=25, ipady=5,pady=25)
boton_salir = tk.Button(contenedor_botones_archivo, text="Salir", command=boton_exit,font=fuente,background="pink" )
boton_salir.pack( ipadx=65, ipady=5,pady=25)
# Centrar el Frame en la ventana
textae = Text(ventana,width=50, height=50,bd=3,background='linen')
text = Text(ventana, width=50, height=50, bd=3,background='linen')
text.pack(padx=10,pady=10,expand=True,fill="both")
textae.pack(padx=10,pady=10, expand=True , fill="both" )
scrollbar_vertical = Scrollbar(text, command=text.yview)
scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
# Agregar una barra de desplazamiento horizontal al Text
scrollbar_horizontal = Scrollbar(text, command=text.xview, orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
scrollbar1_vertical = Scrollbar(textae, command=textae.yview)
scrollbar1_vertical.pack(side=tk.RIGHT, fill=tk.Y)
# Agregar una barra de desplazamiento horizontal al Text
scrollbar1_horizontal = Scrollbar(textae, command=textae.xview, orient=tk.HORIZONTAL)
scrollbar1_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.mainloop()