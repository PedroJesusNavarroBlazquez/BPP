tamMinimo = False

while not tamMinimo:
    password = input("Introduzca una contrasena que contenga al menos 8 caracteres: ")
    if(len(password) > 7):
        tamMinimo = True
    else:
        print("La contrasena es demasiado corta. Debe tener al menos 8 caracteres.")

print("OK, contrasena correcta")