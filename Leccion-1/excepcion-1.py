try:
    fichero = open("numero.txt", "r")
    lines = fichero.readlines()
    print(lines)
except IOError as err:
    print("No encuentro el fichero o no puedo leerlo. Error: ", err)
else:
    print("He leido el fichero sin problemas. Lo cierro y termino.")
    fichero.close()