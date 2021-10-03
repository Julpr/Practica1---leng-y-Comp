#
#   Class: ExpresionMatematica
#
PosicionCinta=0
TokenEntrada=""
cadena=""
CadenaAnalizada=""

def Expresion():
    Termino()
    ExpresionPrima()

def ExpresionPrima():
    global TokenEntrada
    if (TokenEntrada is not None):
        if (TokenEntrada=='+'):
            HacerMatch('+')
            Termino()
            ExpresionPrima()
        else:
            if(TokenEntrada=="-"):
                HacerMatch('-')
                Termino()
                ExpresionPrima()
            else:
                print("Error de sintaxis"+"linea")

def Termino():
    Factor()
    TerminoPrima()


def TerminoPrima():
    global TokenEntrada
    if (TokenEntrada is not None):
        if (TokenEntrada == '*'):
            HacerMatch('*')
            Factor()
            TerminoPrima()
        else:
            if (TokenEntrada == '/'):
                HacerMatch('/')
                Factor()
                TerminoPrima()
            else:
                return

def Factor():
    global TokenEntrada
    if (TokenEntrada is not None):
        if(TokenEntrada.isdigit()):
            Numero()

def HacerMatch(t):
    global TokenEntrada
    if (TokenEntrada is not None):
        if(t!=TokenEntrada):
            print("se esperaba "+t)
        else:
            TokenEntrada=obtenerToken()


def Numero():
    Digito()
    NumeroPrima()


def NumeroPrima():
    global TokenEntrada
    if (TokenEntrada is not None):
        if (TokenEntrada.isdigit()):
            Digito()
            NumeroPrima()
        else:
            return


def Digito():
    global TokenEntrada
    if (TokenEntrada is not None):
        if (TokenEntrada.isdigit()):
            HacerMatch(TokenEntrada)
        else:
            print("Error de sintaxis")


def obtenerToken():
    global PosicionCinta, CadenaAnalizada
    if(PosicionCinta<len(CadenaAnalizada)):
        PosicionCinta = PosicionCinta + 1
        return (CadenaAnalizada[PosicionCinta-1])
    else:
        return None

def funcionPrinncipal(cadena):
    global PosicionCinta, CadenaAnalizada, TokenEntrada
    PosicionCinta=0
    CadenaAnalizada = cadena
    TokenEntrada=obtenerToken()
    Expresion()
    return 0