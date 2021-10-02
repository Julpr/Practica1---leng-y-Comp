from tkinter import *
from tkinter import filedialog as FileDialog, messagebox, ttk
from io import open
from AnalisisLexico import *
from ExpresionMatematica import funcionPrinncipal

# Inicializamos la ruta del fichero como vacía
ruta = "" 

#funcion de las opciones del menu superior
def nuevo():
    global ruta
    #mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("analizador lexico")

def abrir():
    global ruta
    #mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0,'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta)

def guardar():
    #mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
      # mensaje.set("Fichero guardado correctamente")
    else:
        guardar_como()

def guardar_como():
    global ruta
    #mensaje.set("Guardar fichero como")

    fichero = FileDialog.asksaveasfile(title="Guardar fichero",
        mode="w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0,'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
     #   mensaje.set("Fichero guardado correctamente")
    else:
      #  mensaje.set("Guardado cancelado")
        ruta = ""

# Acá se ejecuta el analisis lexico que se encuentra en el archivo AnalisisLexico.py
def analisisLexico():
    tabla.delete(*tabla.get_children())
    tabla2.delete(*tabla.get_children())
    if (ruta!=""):
        funAnlisis(ruta,tabla,tabla2)
        frame.pack(padx=0, pady=0, ipadx=50, ipady=5)
        texto.pack(padx=0, pady=0, ipadx=50, ipady=50)
        tabla.pack(fill="x", expand=1)
        tabla2.pack(fill="x", expand=1)

    else :
        messagebox.showinfo(message="Codigo fuente vacío"+'\n', title="Codigo fuente no encontrado")

def prueba():
    if(ruta!=""):
        texto.pack_forget()
        frame.pack_forget()
        expresion_lista = list(lisExpresionesMatematicas)
        Label(root, text="analisis").pack(fill="x", expand=1)
        for i in range(len(expresion_lista)):
            if(funcionPrinncipal(expresion_lista[i])==0):
                 Label(root, text="la expresion "+expresion_lista[i]+" ").pack(fill="x", expand=1)
            else:
                Label(root, text="la expresion " + expresion_lista[i] + " esta mal escrita").pack(fill="x", expand=1)
    else:
        messagebox.showinfo(message="Codigo fuente vacío"+'\n', title="Codigo fuente no encontrado")

# Configuración de la raíz
root = Tk()
root.title("Analizador lexico")
root.resizable(0,1)
frame = Frame(root)
frame.pack(padx=0, pady=0, ipadx=50, ipady=10)
#frame.pack(side="bottom", fill="x", expand=1)

# Menú superior, donde en la opcion de archivo puedo guardar, guardar como, abrir mi codigo y salir
#en la opcion de analisis puedo ejecutar el analisis lexico, pero solo si existe codigo cargado
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit())
menubar.add_cascade(menu=filemenu, label="Archivo")

menuAnalisis = Menu(menubar, tearoff=0)
menuAnalisis.add_command(label="1- Análisis léxico", command=analisisLexico)
menuAnalisis.add_command(label="2- Análisis de expresiones", command=prueba)
menubar.add_cascade(menu=menuAnalisis, label="Analisis")
root.config(menu=menubar)

# Caja de texto central, aqui puedo escribir mi codigo fuente, vizualizar o editarlo
texto = Text(root)
texto.pack(padx=0, pady=0, ipadx=50, ipady=50)
#texto.pack(fill="x", expand=1) #para ocupar lo que ocupa el padre en ancho

texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))
texto.config(bg = '#fde2b1')

#creo la tabla 1 donde muestro lo del primer taller
tabla = ttk.Treeview(frame)
tabla.pack(fill="x", expand=1)
tabla["columns"] = ("1", "2", "3", "4","5")
tabla['show'] = 'headings'
tabla.column("1", width = 70, anchor ='center')
tabla.column("2", width = 200, anchor ='center')
tabla.column("3", width = 70, anchor ='center')
tabla.column("4", width = 70, anchor ='center')
tabla.column("5", width = 300, anchor ='center')
tabla.heading("1", text ="#")
tabla.heading("2", text ="SIMBOLO")
tabla.heading("3", text ="LINEA")
tabla.heading("4", text ="COLUMNA")
tabla.heading("5", text ="TIPO")

#creo la tabla 2 donde muestro lo de este taller
tabla2 = ttk.Treeview(frame)
tabla2.pack(fill="x", expand=1)
tabla2["columns"] = ("1", "2", "3", "4")
tabla2['show'] = 'headings'
tabla2.column("1", width = 25, anchor ='center')
tabla2.column("2", width = 150, anchor ='center')
tabla2.column("3", width = 80, anchor ='center')
tabla2.column("4", width = 300, anchor ='center')
tabla2.heading("1", text ="#")
tabla2.heading("2", text ="TOKEN")
tabla2.heading("3", text ="ID-TOKEN")
tabla2.heading("4", text ="LEXEMA")

# bucle de la aplicacion
root.mainloop()
