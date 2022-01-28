def comprobarTipoFloat(n):
    if(type(n) != float):
        raise (TypeError, "n debe ser de tipo float")
    else:
        print(f"El numero es {n} de tipo float.")

comprobarTipoFloat(5.2)