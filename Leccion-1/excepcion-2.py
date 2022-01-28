class Error(Exception):
    pass

class ValorDemasiadoPequenoError(Error):
    pass

class ValorDemasiadoGrandeError(Error):
    pass

class ValorIntroducidoNoNumerico(Error):
    pass

numero = 10 


while(True):
    try:
        numero_entrada = int(input("Introduce un numero: "))
        if(type(numero_entrada) != int):
            raise ValueError
        elif(numero_entrada < numero):
            raise ValorDemasiadoPequenoError
        elif(numero_entrada > numero):
            raise ValorDemasiadoGrandeError
        break
    except ValorDemasiadoGrandeError:
        print("El numero es demasiado grande, intentelo de nuevo")
        print()
    except ValorDemasiadoPequenoError:
        print("El numero es demasiado pequeño, intentelo de nuevo")
        print()
    except ValueError:
        print("El valor introducido no es numerico, introduce un numero.")

print(f"Has encontro el numero correcto ({numero}), Enhorabuena !!")