#
#   Class: AnalisisLexico
#
operadoresString= ["operadores ",","," separadores"]
condicionalesString=["condicionales ",","," palabras reservadas"]
#diccionario de los operadores, aqui almaceno el token, el tipo al que pertenece, su ID y su lexema
simbolosOperadores={
'+':{'tipos':operadoresString,'IDtoken':4,'lexema':"suma"},
'-':{'tipos':operadoresString,'IDtoken':5,'lexema':"resta"},
'*':{'tipos':operadoresString,'IDtoken':6,'lexema':"multiplicacion"},
'/':{'tipos':operadoresString,'IDtoken':7,'lexema':"division"}}
#diccionario de los separadores
simbolosSeparadores ={'and':{'tipos':operadoresString,'IDtoken':1,'lexema':"and"},
'or':{'tipos':operadoresString,'IDtoken':2,'lexema':"or"},
'not':{'tipos':operadoresString,'IDtoken':3,'lexema':"not"},
'%':{'tipos':operadoresString,'IDtoken':8,'lexema':"modulo"},
'>':{'tipos':operadoresString,'IDtoken':9,'lexema':"mayorQue"},
'<':{'tipos':operadoresString,'IDtoken':10,'lexema':"menorQue"},
'=':{'tipos':operadoresString,'IDtoken':11,'lexema':"igual"},
'(':{'tipos':operadoresString,'IDtoken':12,'lexema':"parentesisIzq"},
')':{'tipos':operadoresString,'IDtoken':13,'lexema':"parentesisDer"},
'"':{'tipos':"separador",'IDtoken':14,'lexema':"comillas"},
' ':{'tipos':"separador",'IDtoken':15,'lexema':"espacioVacio"},
'   ':{'tipos':"separador",'IDtoken':16,'lexema':"tab"},
'\n':{'tipos':"separador",'IDtoken':17,'lexema':"saltoDeLinea"},
';':{'tipos':"separador",'IDtoken':18,'lexema':"punto&coma"},
':':{'tipos':"separador",'IDtoken':19,'lexema':"dosPuntos"}}
#se agregan los operadores a los separadores, ya que estos hacen parte de los separadores

simbolosSeparadores.update(simbolosOperadores)

#Diccionario de las palabras reservadas

SimbolosReservados={
'for':{'tipos':condicionalesString,'IDtoken':19,'lexema':"for"},
'if':{'tipos':condicionalesString,'IDtoken':20,'lexema':"if"},
'else':{'tipos':condicionalesString,'IDtoken':21,'lexema':"else"},
'while':{'tipos':condicionalesString,'IDtoken':22,'lexema':"while"},
'print':{'tipos':"palabra reservada",'IDtoken':23,'lexema':"imprimirPorPantalla"},
'class':{'tipos':"palabra reservada",'IDtoken':24,'lexema':"class"},
'def':{'tipos':"palabra reservada",'IDtoken':25,'lexema':"def"},
'default':{'tipos':"palabra reservada",'IDtoken':26,'lexema':"default"},
'break':{'tipos':"palabra reservada",'IDtoken':27,'lexema':"break"},
'return':{'tipos':"palabra reservada",'IDtoken':28,'lexema':"return"},
'int':{'tipos':"palabra reservada",'IDtoken':28,'lexema':"int"},
'char':{'tipos':"palabra reservada",'IDtoken':28,'lexema':"char"},
'String':{'tipos':"palabra reservada",'IDtoken':28,'lexema':"String"},
            }
#se crea lista de los diccionarios de los simbolos conocidos con las llaves para identificarlas mas f??cil en el codigo fuente
listSimOper = list(simbolosOperadores.keys())
listSimReservados = list(SimbolosReservados.keys())
listSimSeparador = list(simbolosSeparadores.keys())
lisExpresionesMatematicas = []

#
#   	Function: funVerificarSimb
#  
#  		Verifica si pertenece a las palabras reservadas.
#
#       Parameters:
#       string - Cadena que se comparar?? con el par??metro <simbolo>
#       simbolo - S??mbolo que se comparar?? con el par??metro <string>
#
def funVerificarSimb(string, simbolo):
    i=0
    if(len(string) == len(simbolo)):
        while (i < len(string)   and string[i]==simbolo[i]):
            i=i+1
        if(i< len(string)):
            return -1
        else: return 1
    else: return -1

#
#   	Function: FunGuardarSim
#  
#  		Guardar?? los s??mbolos que sean del lenguaje (Incluyendo los separadores).
#
#       Parameters:
#       subCad - Cadena que se insertar?? en las tablas
#       c - Auxiliar
#       linea - Ubicaci??n con respecto a la linea
#       ubicacionSim - Ubicaci??n con respecto a la columna
#       tabla - Tabla superior mostrada en la interfaz
#       tabla2 - Tabla inferior mostrada en la interfaz
#       sentencia - Se evaluar?? para saber si corresponde a una expresi??n matem??tica
#
def FunGuardarSim(subCad, c, linea, ubicacionSim, tabla,tabla2, sentencia):
    i=0
    l=linea-1
    while(i < len(listSimReservados) and funVerificarSimb(subCad, listSimReservados[i]) != 1):
        i=i+1
    if (i< len(listSimReservados)):
        # agregando a tablas los datos del primer taller y segundo
        tabla.insert("", 'end',values=("-",SimbolosReservados[subCad]['tipos'],linea, ubicacionSim - len(subCad),subCad))
        tabla2.insert("", 'end',values=("-",SimbolosReservados[subCad]['lexema'],SimbolosReservados[subCad]['IDtoken'],subCad))
    if (c!="" and c!="\n"):
        #agregando a tablas los datos del primer taller y segundo
        tabla.insert("", 'end',values=("-",simbolosSeparadores[c]['tipos'],linea, ubicacionSim,c))
        tabla2.insert("", 'end',values=("-", simbolosSeparadores[c]['lexema'],simbolosSeparadores[c]['IDtoken'],c))
        #para saber si hay una expresion matem??tica
        if(funIsOperador(c)==-1 and c!="\n" ):
            lisExpresionesMatematicas.append(sentencia[0:len(sentencia)-1])

#
#   	Function: funIsOperador
#  
#  		Revisa si se est?? sobre un operador, con esto nos apoyaremos para saber 
#       si hay o no, una expresi??n matem??tica
#
#       Parameters:
#       c - Caracter que ser?? comparado con un operador matem??tico.
#
def funIsOperador(c):
    for s in listSimOper:
        if c==s:
            return -1

#funcion que evalua si hay un separador, si es asi retorna -1.
#   	Function: funIsOperador
#  
#  		Revisa si se est?? sobre un operador, con esto nos apoyaremos para saber si 
#       hay o no, una expresi??n matem??tica
#
#       Parameters:
#       c - Caracter que ser?? comparado con un operador matem??tico.
#
def funIsSeparador(c):
    for s in listSimSeparador:
        if c==s:
            return -1


#   	Function: funSeparar
#  
#  		Separa las palabras de c??digo fuente, seg??n los separadores, para 
#       posteriormente ser evaluadas y as?? saber si
#       es una palabra reservada del lenguaje
#
def funSeparar(c,k,tabla,tabla2):
    subCad=""
    for i in range(0,len(c)):
        if (funIsSeparador(c[i])!=-1):
            subCad+=c[i]
        else:
            FunGuardarSim(subCad,c[i],k,i,tabla,tabla2,c)
            subCad=""
    if(subCad!=""):
        FunGuardarSim(subCad,"",k,i+1,tabla,tabla2,c)


#Se lee el archivo "codigoFuente" donde se encuentra el codigo a analizar
#Se lee l??nea por l??nea y se pasa cada l??nea a la funci??n "funSeparar()" donde se separan las palabras

#   	Function: funAnlisis
#  
#  		Lee el archivo pasado como par??metro l??nea por l??nea, donde cada una se estas se pasar??n a la funci??n <funSeparar>, donde 
#       se separar??n por palabras
#
#       Parameters:
#       codigoFuente - Archivo donde se encuentra el c??digo que se analizar??
#       tabla - Tabla superior mostrada en la interfaz
#       tabla2 - Tabla inferior mostrada en la interfaz
#
def funAnlisis(codigoFuente,tabla,tabla2):
    lisExpresionesMatematicas.clear()
    codigoFuente = open(codigoFuente, "r")
    linea = codigoFuente.readline()  # lee la primera l??nea
    k=0; z=0
    while linea != "": #hasta que no haya mas l??nea,se ignora cualquier espacio, tabulador o enter.
        funSeparar(linea,k+1,tabla,tabla2)
        linea = codigoFuente.readline()
        k=k+1
    codigoFuente.close()
    #se muestro lista con las posibles expresiones matematicas

