import numpy as np

def checklist(lst):
    elem = lst[0]
    resultado = True
    for i in range(1, len(lst)):
        if(lst[i] != elem):
            resultado = False

    return resultado

def tragaperras():
    opciones = ["cereza", "uva", "manzana", "melon",  "naranja"]

    tirada  = np.random.randint(0, len(opciones), size=len(opciones))
    print("El resultado de su tirada es: ")
    for i in tirada:
        print(opciones[i])

    resultado = checklist(tirada)
    if(resultado):
        print("Ha ganado el premio")
    else:
        print("Mala suerte, intentelo de nuevo")



tragaperras()
