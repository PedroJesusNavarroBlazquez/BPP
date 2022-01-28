def leer_enteros():
    num_intentos = 0
    while(num_intentos < 3):
        n = input("Introduzca un numero entero: ")
        try:
            n = int(n)
            print("n es: ", n)
        except ValueError:
            num_intentos += 1
    
    raise(ValueError, "Has ingresado un valor incorrecto en tres ocasiones. Se acabaron tus oportunidades.")

leer_enteros()