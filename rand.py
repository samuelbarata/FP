def tab_string(t):
    """tuplo-->lista"""
    t = list(t)
    for i in range(len(t)):
        t[i] = list(t[i])
    return t

def tab_tuplo(t):
    """lista-->tuplo"""
    for i in range(len(t)):
        t[i] = tuple(t[i])
    return tuple(t)

import random
def tabulairo_random():
    """cria um tabuleiro random para testar funcoes"""
    t1=(rand(),rand(),rand())
    t2=(rand(),rand(),rand())
    t3=(rand(),rand())
    return (t1, t2, t3)
    
def rand():
    return random.randint(-1,1)

def untab_rand():
    """cria um tabuleiro invalido para testar funcoes"""
    u = (True,False,random.randint(10,500),random.randint(-9,-2),chr(random.randint(97,122)),"dell")
    i = random.randint(0,2)
    if i == 2:
         j = random.randint(0,1)
    else:
        j = random.randint(0,2)
    k = tab_string(tabulairo_random())
    a = random.randint(0, len(u)-1)
    if a == len(u)-1:
        k = [(k[random.randint(0, 2)]), (k[random.randint(0, 2)])]
    else:
        k[i][j] = u[a]
    return tab_tuplo(k)
