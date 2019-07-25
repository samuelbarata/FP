#94230 Samuel Barata

#_________________CELULAS_________________#
#Celulas sao definidas como [-1], [0], [1]
def cria_celula(v):
    """
    cria_celula: int --> celula
    Recebe um estado {0,1,-1} e devolve uma célula com esse valor
    """
    if not (type(v) == int and v in (-1, 0, 1)):
        raise ValueError("cria_celula: argumento invalido.")
    return [v]
#----

def obter_valor(c):
    """
    obter_valor: celula --> {-1,0,1}
    Recebe uma celula e devolve o seu estado {0,1,-1}
    """
    return c[0]
#----

def inverte_estado(c):
    """
    inverte_estado: celula --> celula
    Recebe o valor de uma celula e devolve o estado inverso (ativo -> inativo, inativo -> ativo, 
    indeterminado -> indeterminado)
    """
    c[0] = ((c[0] + 1) % 2 if c[0] >= 0 else c[0])
    return c  # destrutiva
#----

def eh_celula(arg):
    """
    eh_celula: universal --> bool
    Recebe um argumento e verifica se e uma celula
    """
    try:
        return type(arg) == list and (arg[0] in (0,1,-1)) and len(arg) == 1
    except:
        return False
#----

def celulas_iguais(c1, c2):
    """
    celulas_iguais: celula^2 --> bool
    Verifica se 2 celulas sao iguais
    """
    return eh_celula(c1) and eh_celula(c2) and c1 == c2
#----

def celula_para_str(c):
    """
    celula_para_str: celula --> str
    Converte o valor de uma celula numa string (I -> '0', A --> '1', X -> 'x')
    """
    return str(obter_valor(c)) if obter_valor(c) >= 0 else 'x'
#----

#_________________COORDENADA_________________#
#coordenadas sao definidas como tuplos (linha, coluna)
def eh_coordenada(arg):
    """
    eh_coordenada: universal --> bool
    Recebe um argumento e verifica se e uma coordenada
    """
    return (type(arg) == tuple and len(arg)==2 and\
    type(arg[0]) == type(arg[1]) == int and\
    0 <= arg[0] <= 2 and 0 <= arg[1] <= 2)
#----

def cria_coordenada(l,c):
    """
    cria_coordenada: N^2 --> coordenada
    Recebe uma linha e coluna de uma matrix 3x3 e converte em coordenadas
    """
    if eh_coordenada((l, c)):
        return (l,c)
    raise ValueError("cria_coordenada: argumentos invalidos.")
#----

def coordenada_linha(c):
    """
    coordenada_linha: coordenada --> N
    Devolve a linha da coordenada introduzida
    """
    return c[0]
#----

def coordenada_coluna(c):
    """
    coordenada_coluna: coordenada --> N
    Devolve a linha da coordenada introduzida
    """
    return c[1]
#----

def coordenadas_iguais(c1,c2):
    """
    coordenadas_iguais: coordenada^2 --> bool
    Recebe 2 coordenadas e verifica se sao iguais
    """
    return eh_coordenada(c1) and eh_coordenada(c2) and c1==c2
#----

def coordenada_para_str(c):
    """
    coordenada_para_str: coordenada --> string
    Recebe uma coordenada e escreve-a
    """
    return "({}, {})".format(c[0],c[1])
#----

#_________________TABULEIRO_baixo_nivel________________#
#tabuleiro definido como dicionario com chaves coordenadas e elementos celulas
def tabuleiro_inicial():
    """
    tabuleiro_inicial: {} --> tabuleiro
    Devolve o tabuleiro inicial do jogo
    """
    return str_para_tabuleiro('((-1,-1,-1),(0,0,-1),(0,-1))')
#----

def str_para_tabuleiro(s):
    """
    str_para_tabuleiro: str --> tabuleiro
    Recebe uma string (tuplo de tuplos) e converte em forato de tabuleiro
    """
    if type(s) == str:
        s = eval(s)
    else:
        raise ValueError("str_para_tabuleiro: argumento invalido.")
    if not eh_tabuleiro_proj1(s):
        raise ValueError("str_para_tabuleiro: argumento invalido.")
    return {
        cria_coordenada(0, 0): cria_celula(s[0][0]), cria_coordenada(0, 1): cria_celula(s[0][1]),
        cria_coordenada(0, 2): cria_celula(s[0][2]), cria_coordenada(1, 0): cria_celula(s[1][0]),
        cria_coordenada(1, 1): cria_celula(s[1][1]), cria_coordenada(1, 2): cria_celula(s[1][2]),
        cria_coordenada(2, 1): cria_celula(s[2][0]), cria_coordenada(2, 2): cria_celula(s[2][1])}
#----

def tabuleiro_dimensao(t):
    """
    tabuleiro_dimensao: tabuleiro --> N
    Devolve o numero de linhas/colunas de um dado tabuleiro
    """
    return 3
#----

def tabuleiro_celula(t,coor):
    """
    tabuleiro_celula: tabuleiro, coordenada --> celula
    Recebe um tabuleiro e uma coordenada e devolve o estado da celula correspondente
    """
    return t[coor]
#----

def tabuleiro_substitui_celula(t,cel,coor):
    """
    tabuleiro_substitui_celula: tabuleiro, celula, coordenada --> tabuleiro
    Recebe um tabuleiro uma coordenada e uma celula e substitui a celula existente na coordenada 
    dada pela celula recebida
    """
    if not (valida_coordenada(coor) and eh_celula(cel) and eh_tabuleiro(t)):
        raise ValueError("tabuleiro_substitui_celula: argumentos invalidos.")
    t[coor] = cel  # destrutiva
    return t
#----

def tabuleiro_inverte_estado(t,coor):
    """
    tabuleiro_inverte_estado: tabuleiro, coordenada --> tabuleiro
    Recebe um tabuleiro e uma coordenada e inverte o estado da celula correspondente
    """
    if not(eh_tabuleiro(t) and valida_coordenada(coor)):
        raise ValueError("tabuleiro_inverte_estado: argumentos invalidos.")
    # destrutiva
    return tabuleiro_substitui_celula(t, inverte_estado(tabuleiro_celula(t, coor)), coor)
#----

def eh_tabuleiro(arg):
    """
    eh_tabuleiro: tabuleiro --> bool
    Recebe um tabuleiro e verifica se e um tabuleiro valido ou nao
    """
    TABULEIRO_EXEMPLO = tabuleiro_inicial() #tabuleiro que possui todas as posicoes
    try:
        return type(arg) == type(TABULEIRO_EXEMPLO) and \
            len(arg) == len(TABULEIRO_EXEMPLO) and \
            all(i in TABULEIRO_EXEMPLO for i in arg) and \
            all(eh_celula(arg[i]) for i in arg)
    except:
        return False
#----

def tabuleiros_iguais(t1,t2):
    """
    tabuleiros_iguais: tabuleiro^2 --> bool
    Verifica se 2 dados tabuleiros sao iguais
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1==t2
#----

def tabuleiro_para_str(t):
    """
    tabuleiro_para_str: tabuleiro --> string
    Recebe um tabuleiro e transoforma-o numa string visualmente precetivel
    """
    line = '+-------+\n'
    line += '|...{}...|\n'
    line += '|..{}.{}..|\n'
    line += '|.{}.{}.{}.|\n'
    line += '|..{}.{}..|\n'
    line += '+-------+'
    return line.format(\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(0, 2))),\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(0, 1))),\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(1, 2))),\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(0, 0))),\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(1, 1))),\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(2, 2))),\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(1, 0))),\
        celula_para_str(tabuleiro_celula(t, cria_coordenada(2, 1))))
#----

#_________________TABULEIRO_alto_nivel________________#
def porta_x(t,p):
    """
    porta_x: tabuleiro, {'E','D'} --> tabuleiro
    Devolve o tabuleiro resultante de aplicar a porta X a celula inferior do qubit da esquerda
    ou da direita
    """
    if not (eh_tabuleiro(t) and p in ('E', 'D')):
        raise ValueError("porta_x: argumentos invalidos.")
    if p == 'E':
        CELULAS_A_INVERTER = (cria_coordenada(1, 0), cria_coordenada(1, 1), cria_coordenada(1, 2))
    elif p == 'D':
        CELULAS_A_INVERTER = (cria_coordenada(0, 1), cria_coordenada(1, 1), cria_coordenada(2, 1))
    for i in CELULAS_A_INVERTER:
        tabuleiro_substitui_celula(t, inverte_estado(tabuleiro_celula(t, i)),i)
    return t
#----

def porta_z(t, p):
    """
    porta_z: tabuleiro, {'E','D'} --> tabuleiro
    Devolve o tabuleiro resultante de aplicar a porta Z a celula superior do qubit da esquerda
    ou da direita
    """
    if not (eh_tabuleiro(t) and p in ('E', 'D')):
        raise ValueError("porta_z: argumentos invalidos.")
    if p == 'E':
        CELULAS_A_INVERTER = (cria_coordenada(0, 0), cria_coordenada(0, 1), cria_coordenada(0, 2))
    elif p == 'D':
        CELULAS_A_INVERTER = (cria_coordenada(0, 2), cria_coordenada(1, 2), cria_coordenada(2, 2))
    for i in CELULAS_A_INVERTER:
        tabuleiro_substitui_celula(t, inverte_estado(tabuleiro_celula(t, i)), i)
    return t
#----

def porta_h(t, p):
    """
    porta_h: tabuleiro, {'E','D'} --> tabuleiro
    Devolve o tabuleiro resultante de aplicar a porta H ao qubit da esquerda ou da direita
    """
    if not (eh_tabuleiro(t) and p in ('E', 'D')):
        raise ValueError("porta_h: argumentos invalidos.")
    if p == 'E':
        CELULAS_A_TROCAR =  (cria_coordenada(0,0), cria_coordenada(1,0)),\
                            (cria_coordenada(0,1), cria_coordenada(1,1)),\
                            (cria_coordenada(0,2), cria_coordenada(1,2))
    elif p == 'D':
        CELULAS_A_TROCAR =  (cria_coordenada(0,1), cria_coordenada(0,2)),\
                            (cria_coordenada(1,1), cria_coordenada(1,2)),\
                            (cria_coordenada(2,1), cria_coordenada(2,2))
    for i in CELULAS_A_TROCAR:
        coordenada_troca(t, i[0],i[1])
    return t
#----

#_________________FUNCOES_AUXILIARES_________________#
def coordenada_troca(t, coor1, coor2):
    """
    coordenada_troca: tabela,coordenada^2 --> tabela
    Recebe uma tabela e duas coordenadas e troca os valores das celulas entre si
    """
    cel1 = tabuleiro_celula(t, coor1)
    cel2 = tabuleiro_celula(t, coor2)
    tabuleiro_substitui_celula(t, cel1, coor2)
    tabuleiro_substitui_celula(t, cel2, coor1)
    return t
#----

def valida_coordenada(arg):
    """
    valida_coordenada: universal --> bool
    Recebe um argumento e verifica se e uma coordenada valida
    """
    return eh_coordenada(arg) and not(coordenada_linha(arg) == 2 and coordenada_coluna(arg) == 0)
#----

def eh_tabuleiro_proj1(board):
    """ 
    eh_tabuleiro: universal --> bool
    Recebe um tabuleiro e verifica se e um tabuleiro valido ou nao pelos parametros do projeto 1
    """
    return type(board) == tuple and len(board) == 3 and \
        all(type(e) == tuple for e in board) and \
        all(len(e) == 2 if i == 2 else len(e) == 3 for i, e in enumerate(board)) and \
        all(((n in (0, 1, -1) and type(n) == int) for e in board for n in e))
#---

#_________________FUNCOES_ADICIONAIS_________________#
def hello_quantum(f):
    """
    hello_quantum: string --> bool
    Recebe uma string contendo a descrição do tabuleiro objetivo e do número máximo de jogadas, e
    devolvende verdadeiro se o jogador conseguiu transformar o tabuleiro inicial num tabuleiro
    igual, no número de operações requerido para tal
    """
    #dicionario de funcoes
    switch = {'X': porta_x, 'Z': porta_z, 'H': porta_h}

    content = f.split(':')
    TABULEIRO_OBJETIVO = str_para_tabuleiro(content[0])
    NUMERO_MINIMO_JOGADAS = int(content[1])
    
    #comeca o jogo
    print("Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:")
    print(tabuleiro_para_str(TABULEIRO_OBJETIVO))
    print("Comecando com o tabuleiro que se segue:")
    print(tabuleiro_para_str(tabuleiro_inicial()))
    tab_atual,moves = tabuleiro_inicial(),0
    #loop jogo
    while not tabuleiros_iguais(TABULEIRO_OBJETIVO, tab_atual) and moves < NUMERO_MINIMO_JOGADAS:
        #input
        in_porta = str(input("Escolha uma porta para aplicar (X, Z ou H): "))
        in_qubit = str(input("Escolha um qubit para analisar (E ou D): "))
        #tabuleiro novo
        tab_atual = switch[in_porta](tab_atual, in_qubit)
        moves += 1

        print(tabuleiro_para_str(tab_atual))
    #verifica se o objetivo foi atingido
    if tabuleiros_iguais(TABULEIRO_OBJETIVO, tab_atual):
        print("Parabens, conseguiu converter o tabuleiro em {} jogadas!".format(moves))
    return tabuleiros_iguais(TABULEIRO_OBJETIVO, tab_atual)
#----