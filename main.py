from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import json
from tkinter import Text, Scrollbar, filedialog
def boton_analiza():

    pass
def boton_error():

    pass
def boton_report():

    pass
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

text = Text(ventana, width=100, height=100, bd=3,background='linen')
text.pack(padx=10,pady=10,expand=True,fill="both")
scrollbar_vertical = Scrollbar(text, command=text.yview)
scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
# Agregar una barra de desplazamiento horizontal al Text
scrollbar_horizontal = Scrollbar(text, command=text.xview, orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
ventana.mainloop()

