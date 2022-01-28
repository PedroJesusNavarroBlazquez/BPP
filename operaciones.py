# Herramienta que sirve para reecorrer y trabajar con listas.
import time
from functools import reduce

inicio = time.time()

pares = []

def pares_tradicional():
    for i in range(2000000):
        if (i%2 ==  0):
            pares.append(i)
    fin = time.time()
    print('Tiempo de ejecucion:', fin-inicio )

def pares_compresion():
    inicio = time.time()
    pares_eficientes = [i for i in range(2000000) if i%2==0]
    fin = time.time()
    print('Tiempo de ejecucion con compresion', fin-inicio)


def par_if_else_compresion():
    pares = [print(i, 'es par') if i%2==0 else print(i, 'no es par') for i in range(20)]


def bucle_anidado_tradicional():
    m1 = []
    for i in range(5):
        m1.append([])
        for j in range(5):
            m1[i].append(j)
    print('Tradicional', m1)
def bucle_anidado_compresion():
    m2 = [[j for j in range(5)] for i in range(5)]
    print('Compresion ', m2)

numeros = [1, 2, 3, 4, 5]
def cuadrados_tradicional():
    cuadrados = []
    for i in numeros:
        cuadrados.append(i**2)
    print('Tradicional',cuadrados)

def eleva_cuadrado(n):
    return n**2

pares_tradicional()
pares_compresion()
par_if_else_compresion()
bucle_anidado_tradicional()
bucle_anidado_compresion()
cuadrados_tradicional()




numeros2 = [1,2,3,4,5,6,7,8,9,10]
pares2 = []
for i in numeros2:
    if(i%2==0):
        pares2.append(i)
print(pares2)


def es_par(n):
    return n%2==0

pares3 = list(filter(es_par, numeros2))
print(pares3)


numeros4 = [1,2,3,4,5]

total = 0
for i in numeros:
    total += i

print(total)

def suma(n,m):
    return n+m

resultado = reduce(suma, numeros4)
print(resultado)

