from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import json
from tkinter import Text, Scrollbar, filedialog
from palabra import *
from operaciones_un_valor import * 
from operaciones import *
import os
from graphviz import Digraph

#declaracion de las distintas listas
global numero_fila
global numero_columna
global operaciones_resultantes
global lista_palabras
global lista_errores
global palabras_graficos
global palabras #estas son todas mis palabras reservadas que usare
palabras= ['operaciones', 'operacion', 'valor1', 'valor2', 'suma', 'resta', 'multiplicacion', 'division', 'raiz', 'inverso','potencia',
    'seno', 'coseno', 'tangente', 'mod','configuraciones', 'texto', 'fondo', 'fuente', 'forma',':', '[', '{', ',', '}', ']', '.']

numero_fila=1
numero_columna=1
lista_palabras=[]
operaciones_resultantes=[]
lista_errores=[]
palabras_graficos=[]

def analizador(secuencia):
    global numero_fila
    global numero_columna
    global lista_palabras
    global lista_errores
    global palabras_graficos
    global operaciones_resultantes
    global palabras
    numero_fila=1
    lista_errores=[]
    operaciones_resultantes=[]
    lista_palabras=[]
    palabras_graficos=[]
    palabra=''
    posicion=0
    configuraciones=False
    while secuencia:
        num=secuencia[posicion]
        posicion +=1
        if num == '\"':
            palabra,secuencia= crear_palabra(secuencia[posicion:])
            if palabra and secuencia:
                if palabra.lower() not in palabras:
                    caracteres_no_permitidos = '@!|#$%&()=?¿+-/*_¡-;^ªº€½~°©·'
                    if any(char in palabra for char in caracteres_no_permitidos):
                        continue
                    else:
                        palabras_graficos.append(palabra)
                        print (palabra)
                numero_columna+=1
                if not configuraciones:
                    if palabra.lower() not in palabras:
                            caracteres_no_permitidos = '@!|#$%&()=?¿+-/*_¡-;^ªº€½~°©·'
                            if any(char in palabra for char in caracteres_no_permitidos):
                                continue
                            else:
                                e=Palabra(palabra,numero_fila,numero_columna)
                                lista_errores.append(e)
                p= Palabra(palabra.lower(),numero_fila,numero_columna)    
                lista_palabras.append(p)
                numero_columna+=len(palabra)+1
                posicion=0
                if palabra.lower()=='configuraciones':
                    configuraciones=True
        elif num == '[' or num == ']':#Operaciones Anidadas
            p=Palabra(num,numero_fila,numero_columna)
            lista_palabras.append(p)
            secuencia=secuencia[1:]
            posicion=0
            numero_columna+=1
        elif num.isdigit():#alamcenar digitos
            token,secuencia = crear_numero(secuencia)
            if token and secuencia:
                numero_columna+=1
                p=Palabra(token,numero_fila,numero_columna)
                lista_palabras.append(p)
                numero_columna+=len(str(token))+1
                posicion=0
        #por si el texto trae saltos de lineas tabulaciones para que no falle la aplicacion
        elif num == '\n':                       #saltos de linea
            secuencia = secuencia[1:]
            posicion=0
            numero_columna =1
            numero_fila+=1
        elif num == '\t': #tabulaciones
            numero_columna+=4
            secuencia=secuencia[4:]
            posicion=0
        else: #espacios,comas,llaves
            secuencia=secuencia[1:]
            posicion = 0
            numero_columna+=1


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
                        e=Palabra(num,numero_fila,numero_columna+len(palabra)+1)
                        lista_errores.append(e)
                        
            palabra+=num
    return None,None

def crear_numero(secuencia):
    valornume=''
    posicion=''
    global numero_columna
    ncol=numero_columna
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
                    e=Palabra(num,numero_fila,numero_columna+len(valornume)+1)
                    lista_errores.append(e)
            valornume+=num
            ncol+=1
    return None,None

def operar():
    global operaciones_resultantes
    global lista_palabras
    global numero_columna
    
    operacion = ''
    num1=''
    num2=''
    lista_palabras
    while lista_palabras:
        palabra = lista_palabras.pop(0)
        if palabra.funcionToken(None)=='operaciones':
            operaciones=lista_palabras.pop(0)
        elif palabra.funcionToken(None)=='operacion':
            operacion=lista_palabras.pop(0)
        elif palabra.funcionToken(None)=='valor1':
            num1=lista_palabras.pop(0)
            if num1.funcionToken(None)=='[':
                num1=operar()
        elif palabra.funcionToken(None)=='valor2':
            num2=lista_palabras.pop(0)
            if num2.funcionToken(None)=='[':
                num2=operar()
        if operacion and num1 and num2:
            return (Operaciones(num1,num2,operacion,f'{operacion.getFila()}:{operacion.getColumna()}',f':{num2.getFila()}:{num2.getColumna()}'))
        if operacion and num1 and operacion.funcionToken(None)==('seno'or'coseno'or'tangente'or 'inverso'):
            return (Operaciones_un_valor(num1,operacion,f'{operacion.getFila()}:{operacion.getColumna()}',f':{num1.getFila()}:{num1.getColumna()}'))

def funcionan():
    global operaciones_resultantes
    resultado=[]
    while True:
        operacion=operar()
        if operacion:
            resultado.append(f"{operacion.tipo.funcionToken(None)}: {operacion.funcionToken(None)}")
            operaciones_resultantes.append(operacion)
        else:
            break

    for operacionesr in operaciones_resultantes:
        operacionesr.funcionToken(None)

    textae.delete(1.0, tk.END)  # Borrar el contenido actual de textae
    for res in resultado:
        textae.insert(tk.END, res + '\n')


#ANALIZADOR LEXICO    
def boton_analiza():
    contenido = text.get(1.0, tk.END)
    analizador(contenido)
    funcionan()
    

def boton_error():
    global lista_errores

    # Crear una lista de errores en el formato deseado
    errores_json = []
    for i, error in enumerate(lista_errores, start=1):
        if isinstance(error, Palabra):
            fila=error.getFila()
            columna=error.getColumna()
            error_info = {
                "No": i,
                "descripcion": {
                    "lexema": error.getPalabra(),
                    "tipo": "error lexico",
                    "columna": columna,
                    "fila": fila
                }
            }
            errores_json.append(error_info)

    # Guardar la lista de errores en un archivo JSON
    with open("Resultados_202201989.json", "w") as archivo_errores:
        json.dump({"errores": errores_json}, archivo_errores, indent=4)

    # Mostrar los errores en el widget textae
    textae.delete(1.0, tk.END)  # Borrar el contenido actual de textae
    with open("Resultados_202201989.json", "r") as archivo_errores:
        errores_json = json.load(archivo_errores)
        textae.insert(tk.END, json.dumps(errores_json, indent=4))

#Para graficar



def graficar_operaciones(operaciones_resultantes):
    global palabras_graficos
    dot = Digraph(comment="OPERACIONES")
    dot.attr(label=palabras_graficos[0])
    def graficar_operacion(operacion, parent=None, nodos_creados={}):
        if isinstance(operacion, Operaciones):
            nodo_operacion = f"{operacion.tipo.funcionToken(None)} : {operacion.funcionToken(None)}"
            dot.node(f"{nodo_operacion}",color=f"{palabras_graficos[1]}",shape=f"{palabras_graficos[3]}",fontcolor=f"{palabras_graficos[2]}")
            if parent:
                dot.edge(parent, nodo_operacion)

            # Si valor1 es una operación, llamar recursivamente para graficarlo
            if isinstance(operacion.valor1, (Operaciones, Operaciones_un_valor)):
                graficar_operacion(operacion.valor1, nodo_operacion, nodos_creados)
            else:
                valor1_id = f"valor1_{id(operacion.valor1)}"
                if valor1_id not in nodos_creados:
                    dot.node(f"{valor1_id}", f"{operacion.valor1.funcionToken(None)}",color=f"{palabras_graficos[1]}",shape=f"{palabras_graficos[3]}",fontcolor=f"{palabras_graficos[2]}")
                    nodos_creados[valor1_id] = True
                dot.edge(nodo_operacion, valor1_id)

            # Si valor2 es una operación, llamar recursivamente para graficarlo
            if isinstance(operacion.valor2, (Operaciones, Operaciones_un_valor)):
                graficar_operacion(operacion.valor2, nodo_operacion, nodos_creados)
            else:
                valor2_id = f"valor2_{id(operacion.valor2)}"
                if valor2_id not in nodos_creados:
                    dot.node(f"{valor2_id}", f"{operacion.valor2.funcionToken(None)}",color=f"{palabras_graficos[1]}",shape=f"{palabras_graficos[3]}",fontcolor=f"{palabras_graficos[2]}")
                    nodos_creados[valor2_id] = True
                dot.edge(nodo_operacion, valor2_id)

        elif isinstance(operacion, Operaciones_un_valor):
            nodo_operacion = f"{operacion.tipo.funcionToken(None)} : {operacion.funcionToken(None)}"
            dot.node(f"{nodo_operacion}",color=f"{palabras_graficos[1]}",shape=f"{palabras_graficos[3]}",fontcolor=f"{palabras_graficos[2]}")
            if parent:
                dot.edge(parent, nodo_operacion)

            # Llamar recursivamente para graficar el valor de la operación
            if isinstance(operacion.valor1, (Operaciones, Operaciones_un_valor)):
                graficar_operacion(operacion.valor1, nodo_operacion, nodos_creados)
            else:
                valor1_id = f"valor1_{id(operacion.valor1)}"
                if valor1_id not in nodos_creados:
                    dot.node(f"{valor1_id}", f"{operacion.valor1.funcionToken(None)}",color="{palabras_graficos[1]}",shape="{palabras_graficos[3]}",fontcolor="{palabras_graficos[2]}")
                    nodos_creados[valor1_id] = True
                dot.edge(nodo_operacion, valor1_id)

    for operacion in operaciones_resultantes:
        graficar_operacion(operacion, nodos_creados={})

    dot.render('operaciones_resultantes', view=True)


def boton_report():
    graficar_operaciones(operaciones_resultantes)

    #graficar_operaciones(operaciones_resultantes)




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