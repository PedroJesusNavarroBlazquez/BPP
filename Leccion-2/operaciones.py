def suma(a,b):
    return a+b

def division(a,b):
    if (b == 0):
        b = 1
    return a/b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def elevarNumero(base, exponente):
    return base**exponente

def minimo(lista_numeros):
    valor_minimo = lista_numeros[0]
    for i in lista_numeros:
        if(i < valor_minimo):
            valor_minimo = i
    return valor_minimo

def es_par(n):
    return n%2==0

def operacion_inventada(m,n):
    assert(n > 0)
    if(es_par(n)):
        return m/n-1
    else:
        return m/n