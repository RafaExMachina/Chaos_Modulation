# this module will be imported in the into your flowgraph

import numpy as np
import random

#Mapa tenda  
def tendaInclinada(alfa,Npontos):
    x = [0] * Npontos
    x[0] = np.random.random()*2-1
    for i in range(Npontos - 1):
        if (x[i] < alfa):
            x[i + 1] = (2 / (alfa + 1)) * x[i] + ((1 - alfa) / (alfa + 1))
        elif (x[i] >= alfa):
            x[i + 1] = (2 / (alfa - 1)) * x[i] - ((alfa + 1) / (alfa - 1))
    return x[:Npontos-1]

#gerador aleatorio de uns e menos uns   
def ramdomUmeUm(NumSimbolos):
    mylist = np.random.randint(2, size=NumSimbolos)*2-1
    
    return mylist

#gerador aleatorio de uns e zeros
def ramdomUmezeros(NumSimbolos):
    mylist = np.random.randint(2, size=NumSimbolos)
    
    return mylist

# produto vetor vetor
def prod_vv(x, y):
    """ Retorna o produto  entre x e y """
    produto = []
    for x, y in zip(x, y):
        produto.append(x * y)
    return produto

def DCSK(beta,NumSimbolos,alfa):
    myDCSK=[]
    a=tendaInclinada(alfa,2*beta*NumSimbolos)
    b=ramdomUmeUm(NumSimbolos)
    for i in range(NumSimbolos):
    #mylist[i*len(x[0]):(i+1)*len(x[0])]
        myDCSK[i*2*beta:]=a[i*beta:(i+1)*beta]+prod_vv([b[i]]*beta, a[i*beta:(i+1)*beta])
    return myDCSK

def CSK(beta,NumSimbolos,alfa):

    myCSK = []
    a=tendaInclinada(alfa,2*beta*NumSimbolos)
    b=ramdomUmeUm(NumSimbolos)
    for i in range(NumSimbolos):
    #mylist[i*len(x[0]):(i+1)*len(x[0])]
        myCSK[i*2*beta:]=prod_vv([b[i]]*beta, a[i*beta:(i+1)*beta])
    return myCSK

def COOK(beta,NumSimbolos,alfa):

    myCOOK = []
    a=tendaInclinada(alfa,1*beta*NumSimbolos)
    b=ramdomUmezeros(NumSimbolos)
    for i in range(NumSimbolos):
    #mylist[i*len(x[0]):(i+1)*len(x[0])]
        myCOOK[i*1*beta:]=prod_vv([b[i]]*beta, a[i*beta:(i+1)*beta])
    return myCOOK