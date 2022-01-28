# Dado una lista de n numeros devuelva los que son primos. 

# Importamos el paquete necesario para utilizar reduce
from functools import reduce

# Inicializamos la lista
lista = [3, 4, 8, 5, 5, 22, 13]


def es_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True 

primos = list(filter(es_primo, lista))
print(primos)