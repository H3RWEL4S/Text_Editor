from tkinter import *                        #importamos todas las clases y funciones de Tkinter
from tkinter import filedialog as FileDialog #importa las funciones de dialogo de Tkinter
from io import open                          #funcion para abrir y cerrar archivos o ficheros
#Variable para almacenar la ruta del archivo o fichero actual
ruta = "" 

#Crear archivo sin contenido
def nuevo():
    global ruta                               #ovtenemos la ruta actual
    mensaje.set("Nuevo archivo")              #muestra mensaje de estado en la GUI
    ruta = ""                                 #establece la variable ruta en una cadena vacia para evitar archivos abiertos
    texto.delete(1.0, "end")                  #se utiliza para mostrar y editar el contenido del fichero
    root.title("Editor de texto")             #cambia el titulo de la ventana principal a root.title()

#abrir archivo usando el dialogo de seleccion de archivos del S.O
def abrir():
    global ruta                               #nombre del directorio o la ruta
    mensaje.set("Abrir archivo")              #Mensaje establecido dentro del editor
    #Utiliza el dialogo de archivos de Tkinter para que el User elija el archivo a abrir
    ruta = FileDialog.askopenfilename(
        initialdir='.',                       #establecemos directorio
        filetype=( ("Archivos de texto", ".txt"), ), #limita la seleccion de archivos con extension .txt
        title="Abrir Archivo de Texto")       #Establece el titulo del dialogo de seleccion de archivos
    #verificar ruta establecida
    if ruta != "":                            #validamos si tiene una ruta con cadena vacia
        fichero = open(ruta, 'r')             #abre el archivo especificado en modo lectura
        contenido = fichero.read()            #abre todo el contenido y se almacena en contenido
        texto.delete(1.0, 'end')              #borra todo el contenido en el area de texto
        texto.insert('insert', contenido)     #inserta el contenido del archivo leido en la posicion actual del texto
        fichero.close()                       #cierra el archivo abierto previamente
        root.title(ruta + " - Editor de texto") #cambia el titulo de la ventana principal

#Guarda el contenido del área de texto en el fichero actualmente abierto
def guardar():
    #global ruta
    mensaje.set("Guardar archivo")
    #comprovacion de ruta
    if ruta != "":                            #validamos si tiene una ruta con cadena vacia
        contenido = texto.get(1.0, 'end-1c')  #Obtiene el contenido completo del area de texto
        fichero = open(ruta, 'w+')            #abre el archivo especificado por la ruta en modo lectura y escritura
        fichero.write(contenido)              #escribe el contenido en el archivo abierto
        fichero.close()                       #cierra el archivo abierto previamente
        mensaje.set("Archivo se ha guardado correctamente") #mensaje de confirmacion
    else:
        guardar_como()                        #seleccion de nueva ubicacion en caso que no halla texto o sea nuevo el archivo

#Abre un diálogo para guardar el fichero con un nombre y una ubicación nuevos
def guardar_como():
    global ruta
    mensaje.set("Guardar archivo como")
    #especificar un nombre de un nuevo archivo en modo escritura
    fichero = FileDialog.asksaveasfile(title="Guardar archivo", mode="w",
                                       defaultextension=".txt")
    if fichero is not None:                   #validacion de valores
        ruta = fichero.name                   #almacena nombre completo del archivo en ruta
        contenido = texto.get(1.0, 'end-1c')  #obtiene el contenido completo del area de texto
        fichero = open(ruta, 'w+')            #abre el archivo en modo escritura y lectura
        fichero.write(contenido)              #escribe el contenido en el archivo abierto
        fichero.close()                       #cierra el archivo
        mensaje.set("Archivo se ha guardado correctamente") #mensaje de confirmacion
    else:
        mensaje.set("Almacenamiento cancelado") #mensaje de cancelacion
        ruta = ""                             #indicamos que no hay archivo guardado

#root
root = Tk()
root.title("Editor de texto") #titulo de la ventana

#Menu Superiro
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como...", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

#TextBox
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config( bd=0, padx=6, pady=4, font=("Consolas", 12) )

#Monitor inferior de Sublime
mensaje = StringVar()
mensaje.set("Bienvenidoa  tu editor")
monitor = Label(root, textvariable=mensaje, justify="left")
monitor.pack(side="left")

#
root.config(menu=menubar)

#bucle del app
root.mainloop()