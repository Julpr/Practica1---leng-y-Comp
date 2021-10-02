operadoresString= ["operadores ",","," separadores"]
condicionalesString=["condicionales ",","," palabras reservadas"]
#diccionario de los operadores, aqui almaceno el toke, el tipo al que pertenece, su ID y su lexema
simbolosOperadores={'+':{'tipos':operadoresString,'IDtoken':4,'lexema':"suma"},
'-':{'tipos':operadoresString,'IDtoken':5,'lexema':"resta"},
'*':{'tipos':operadoresString,'IDtoken':6,'lexema':"multiplicacion"},
'/':{'tipos':operadoresString,'IDtoken':7,'lexema':"divicion"}}
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
'\n':{'tipos':"separador",'IDtoken':16,'lexema':"saltoDeLinea"},
';':{'tipos':"separador",'IDtoken':17,'lexema':"punto&coma"},
':':{'tipos':"separador",'IDtoken':18,'lexema':"dosPuntos"}}
#agrego los operadores a los separadores, ya que estos hacen parte de los separadores
simbolosSeparadores.update(simbolosOperadores)
#diccionario de las palabras reservadas
SimbolosReservados={
'for':{'tipos':condicionalesString,'IDtoken':19,'lexema':"for"},
'if':{'tipos':condicionalesString,'IDtoken':20,'lexema':"if"},
'else':{'tipos':condicionalesString,'IDtoken':21,'lexema':"else"},
'elif':{'tipos':condicionalesString,'IDtoken':22,'lexema':"elif"},
'while':{'tipos':condicionalesString,'IDtoken':23,'lexema':"while"},
'do':{'tipos':condicionalesString,'IDtoken':24,'lexema':"do"},
'def':{'tipos':"palabra reservada",'IDtoken':25,'lexema':"definirFuncion"},
'print':{'tipos':"palabra reservada",'IDtoken':26,'lexema':"imprimirPorPantalla"},
            }
#creo lista de los diccionarios de los simbolos conocidos con las llaves para ayudarme a identificarlas mas facil en el codigo fuente
listSimOper = list(simbolosOperadores.keys())
listSimReservados = list(SimbolosReservados.keys())
listSimSeparador = list(simbolosSeparadores.keys())
lisExpresionesMatematicas = []

# verifico si pertenece a las palabras reservadas
def funVerificarSimb(string, simbolo):
    i=0
    if(len(string) == len(simbolo)):
        while (i < len(string)   and string[i]==simbolo[i]):
            i=i+1
        if(i< len(string)):
            return -1
        else: return 1
    else: return -1

#guardo los simbolos que sean del lenguaje incluyendo los separadores
def FunGuardarSim(subCad, c, linea, ubicacionSim, tabla,tabla2, sentencia):
    i=0
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
        #para saber si hay una expresion matematica
        if(funIsOperador(c)==-1 and c!="\n"):
            lisExpresionesMatematicas.append(sentencia[0:len(sentencia)-1])



#para saber si estoy parado sobre un operador, esto me ayuda a la hora de saber si estoy en un expresion matematica
def funIsOperador(c):
    for s in listSimOper:
        if c==s:
            return -1

#funcion que evalua si hay un separador, si es asi retorna -1.
def funIsSeparador(c):
    for s in listSimSeparador:
        if c==s:
            return -1

#me separa las palabras de mi codigo fuente, segun los separadores, para luego ser evaluadas
#si es o no una palabra reservada del lenguaje
def funSeparar(c,k,tabla,tabla2):
    subCad=""
    for i in range(0,len(c)):
        #print (c,end="")
        if (funIsSeparador(c[i])!=-1):
            subCad+=c[i]
        else:
            FunGuardarSim(subCad,c[i],k,i,tabla,tabla2,c)
            subCad=""
    if(subCad!=""):
        FunGuardarSim(subCad,"",k,i+1,tabla,tabla2,c)


#leo el archivo "codigoFuente" donde se encuentra el codigo a analisar
#se lee linea por linea y se pasa cada linea a la funcion "funSeparar()" donde separo las palabras

def funAnlisis(codigoFuente,tabla,tabla2):
    lisExpresionesMatematicas.clear()
    codigoFuente = open(codigoFuente, "r")
    linea = codigoFuente.readline()  # lee la primera línea
    k=0; z=0
    while linea != "": #hasta que no haya mas linea, de aqui en adelante se ignora cualquier espacio, tabulador o enter
        funSeparar(linea,k+1,tabla,tabla2)
        linea = codigoFuente.readline()
        k=k+1
    codigoFuente.close()
    #muestro lista con las posibles expresiones matematicas
    #[sentencia,linea,columna]
    print(lisExpresionesMatematicas)
