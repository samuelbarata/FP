#94230 Samuel Barata


def eh_tabuleiro(t):
    """
    Recebe um tabuleiro ((x,x,x),(x,x,x),(x,x)) (tuplo)
    Avalia se e um tabulairo valido ou nao
    Devolve um booleano True se for valido e False se nao for
    """
    #verifica se recebe um tuplo com 3 elementos
    if not (isinstance(t,tuple) and len(t)==3):return False
    #verifica se todos esses elementos sao tuplos
    for i in range(len(t)):
        if not(isinstance(t[i], tuple)):return False
    #verifica se esses tuplos tem o comprimento adequado para um tauleiro
    if len(t[0]) != 3 or len(t[1]) != 3 or len(t[2]) != 2:return False
    #verifica se cada um desses elementos e um inteiro e 0 1 ou -1
    for i in range(len(t)):
        for k in range(len(t[i])):
            if not ((t[i][k] == 0 or t[i][k] == 1 or t[i][k] == -1)and(type(t[i][k])==int)):return False
    return True
#----

def tab_string(t):
    """
    Recebe um tabuleiro em tuplo
    Devolve um tabuleiro em lista
    """
    t = list(t)
    for i in range(len(t)):
        t[i] = list(t[i])
    return t
#----

def tab_tuplo(t):
    """
    Recebe um tabuleiro em lista
    Devolve o tabuleiro em tuplo
    """
    for i in range(len(t)):
        t[i] = tuple(t[i])
    return tuple(t)
#----

def tabuleiro_str(t):
    """
    Devolve uma string do tabuleiro com o formarto:
    +-------+   Representacao:
    |...X...|    0  -->  '0'
    |..X.X..|    1  -->  '1'
    |.X.X.X.|   -1  -->  'x'
    |..X.X..|
    +-------+
    """
    #verifica se e um tabuleiro valido
    if not eh_tabuleiro(t):
        raise ValueError("tabuleiro_str: argumento invalido")
    t = tab_string(t)
    #percorre todos os elementos do tabuleiro e converte-os a strings, trocando -1 por 'x'
    for i in range(len(t)):
        for k in range(len(t[i])):
            if t[i][k] == -1:
                t[i][k] = 'x'
            else:
                t[i][k] = str(t[i][k])
    return "+-------+\n|..."+t[0][2]+"...|\n|.."+t[0][1]+"." +t[1][2]+"..|\n|." +t[0][0]+ "."+t[1][1]+"."+t[2][1]+".|\n|.."+t[1][0]+"."+t[2][0]+"..|\n+-------+"
#----

def tabuleiros_iguais(a,b):
    """
    Recebe 2 tabuleiros (2 tuplos)
    Compara-os se forem validos
    Devolve um booleano True se forem iguais e False se nao forem
    """
    if not (eh_tabuleiro(a) and eh_tabuleiro(b)):
        raise ValueError("tabuleiros_iguais: um dos argumentos nao e tabuleiro")
    return a==b
#----

def invert(a):
    """
    Recebe 0 e 1 e coverte respetivamente em 1 e 0
    Se receber outro valor (ex -1), esse valor permanece inalterado
    Devolve esse valor
    """
    if a == 0: return 1
    if a == 1: return 0
    return a
#----

def porta_x(t,d):
    """
    Recebe um tabuleiro (t) e uma direcao ('D'/'E')
    Inverte os respetivos valores com recurso a funcao 'invert(a)' e 'porta_xz(porta,t,d) se o tabuleiro fornecido for valido
    Devolve o tuplo do respetivo tabuleiro
    Exemplo: porta_x(t, 'E')
    +-------+   +-------+
    |...?...|   |...?...|
    |..?.x..|-->|..?.x..|
    |.?.1.?.|-->|.?.0.?.|
    |..0.?..|   |..1.?..|
    +-------+   +-------+
    """
    if not (eh_tabuleiro(t) and (d == 'E' or d=='D')):
        raise ValueError("porta_x: um dos argumentos e invalido")
    return porta_xz('x',t,d)
#----
    
def porta_z(t,d):
    """
    Recebe um tabuleiro (t) e uma direcao ('D'/'E')
    Inverte os respetivos valores com recurso a funcao invert(a) e porta_xz(porta,t,d) se o tabuleiro fornecido for valido
    Devolve o tuplo do respetivo tabuleiro
    Exemplo: porta_z(t, 'E')
    +-------+   +-------+
    |...x...|   |...x...|
    |..1.?..|-->|..0.?..|
    |.0.?.?.|-->|.1.?.?.|
    |..?.?..|   |..?.?..|
    +-------+   +-------+
    """
    if not (eh_tabuleiro(t) and (d == 'E' or d=='D')):
        raise ValueError("porta_z: um dos argumentos e invalido")
    return porta_xz('z',t,d)  
#----
    
def porta_xz(porta,t,d):
    """
    Recebe a porta (x ou z) e o tabuleiro e direcao vindos das funcoes porta_x e porta_z
    Devolve o tuplo do tabuleiro correspondente a essa alteracao
    """
    #define os parametros para as portas x e z [comentados nas linhas 142;143;148;149]
    if porta == 'x':
        z=1
        y=1
    else:
        z=0
        y=2
    t = tab_string(t)    
    if d == 'E':  
        for i in (0,1,2):
            #x t[1][i] = invert(t[1][i])
            #z t[0][i] = invert(t[0][i])
            t[z][i] = invert(t[z][i])
        return tab_tuplo(t)
    elif d == 'D':
        for i in (0,1):
            #x t[i][1] = invert(t[i][1])
            #z t[i][2] = invert(t[i][2])
            t[i][y] = invert(t[i][y])
        t[2][y-1] = invert(t[2][y-1])
        return tab_tuplo(t)
#----

def porta_h(t,d):
    """
    Recebe um tabuleiro (t) e uma direcao ('D'/'E')
    Inverte 2 linhas ou colunas de acordo com a direcao caso o tabuleiro seja valido
    Devolve o tuplo do tabuleiro correspondente a essa alteracao
    Exemplo: porta_h(t, 'E')
    +-------+   +-------+
    |...0...|   |...x...|
    |..x.x..|-->|..1.0..|
    |.1.1.?.|-->|.0.x.?.|
    |..0.?..|   |..1.?..|
    +-------+   +-------+
    """
    if not (eh_tabuleiro(t) and (d == 'E' or d=='D')):
        raise ValueError("porta_h: um dos argumentos e invalido")
    #Esquerda
    if d == 'E': return (t[1],t[0],t[2])
    #Direita
    else: return ((t[0][0], t[0][2], t[0][1]), (t[1][0], t[1][2], t[1][1]), (t[2][1], t[2][0]))
#----