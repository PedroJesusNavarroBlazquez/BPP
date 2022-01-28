# Compresion de listas.
# El programa debe devolver el mayor elemento de cada sublista (señalado en negrita).

import pdb

# Inicializamos la lista
lista = [[1,2,3,4,5,6,7,8,9,10],[3,50,8,215,165,1,651,65448,52],[100,90,80,70,50,101]]

# Ejemplo tradicional
mayores = []
for l in lista:
    mayores.append(max(l))
print('Tradicional', mayores)


# Ejemplo de como seria con map
def numero_mayor(n):
    return max(n)

mayores = list(map(numero_mayor, lista))
print('Map ',mayores)

# Ejemplo como seria con compresion

# Encontramos el maximo de cada sublista de nuestra lista.

def mayor_compresion():
    pdb.set_trace()
    mayor = [max(sublist) for sublist in lista]
  
    # Imprimimos la lista con todos los valores maximos de cada sublsita.
    print('Comprension ',mayor)

mayor_compresion()
