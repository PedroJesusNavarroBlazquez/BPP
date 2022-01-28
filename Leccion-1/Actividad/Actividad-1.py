import pandas as pd
import matplotlib.pyplot as plot
import numpy as np

class Error(Exception):
    pass

class contenidoColumnas(Error):
    pass

try:
   csv = pd.read_csv('finanzas2020.csv', delimiter=',')
   total_cols=len(csv.axes[1])
   df = pd.DataFrame(csv)
   if(total_cols != 12):
       print(total_cols)
       raise ValueError
   for column in df:
       if df[column].count() == 0:
            raise(contenidoColumnas)
except IOError as err:
    print("No encuentro el fichero o no puedo leerlo. Error: ", err)
except ValueError:
    print("El archivo no tiene 12 columnas.")
except contenidoColumnas:
    print("Hay columnas vacias")


for key,value in df.iteritems():
    for i in range(0, 100):
        if type(value[i])!=int:
            try:
                df.at[i, key] = int(value[i])
                #value[i] = int(value[i])
            except ValueError:
                print(f"El valor {value[i]} no se puede convertir a int, por lo que pasara a valer 0")
                # value[i] = int(0)
                df.at[i, key] = 0
# result = df.tail(40)
# print(result)

# Creamos la lista que almacena el header del dataframe('Enero', 'Febrero',...,'Diciembre)
indices = df.columns.tolist()

# Creamos el diccionario con los valores negativos.
diccionarioN = {indices[0]: 0, indices[1]:0, indices[2]: 0, indices[3]: 0, indices[4]: 0, indices[5]: 0, indices[6]: 0, indices[7]: 0, indices[8]: 0, indices[9]: 0, indices[10]: 0, indices[11]: 0}
for i in indices:
    diccionarioN[i] = df[i].loc[df[i] < 0].sum()
print('')
print('DICCIONARIO CON GASTOS')
print(diccionarioN)
max_key = min(diccionarioN, key=diccionarioN.get)
print(f'El mes que mas dinero se ha gastado es: {max_key}, con un gasto total de {diccionarioN[max_key]}')


# Creamos el diccionario con los valores positivos
print('')
print('DICCIONARIO CON INGRESOS')
diccionarioP = {indices[0]: 0, indices[1]:0, indices[2]: 0, indices[3]: 0, indices[4]: 0, indices[5]: 0, indices[6]: 0, indices[7]: 0, indices[8]: 0, indices[9]: 0, indices[10]: 0, indices[11]: 0}
for i in indices:
    diccionarioP[i] = df[i].loc[df[i] > 0].sum()
print(diccionarioP)

# Creamos el diccionario que alberga la diferencia entre los gastos y los ingresos.
print('')
print('DICCIONARIO CON DIFERENCIA')
diccionarioD = {indices[0]: 0, indices[1]:0, indices[2]: 0, indices[3]: 0, indices[4]: 0, indices[5]: 0, indices[6]: 0, indices[7]: 0, indices[8]: 0, indices[9]: 0, indices[10]: 0, indices[11]: 0}
for i in indices:
    diccionarioD[i] = diccionarioP[i] + diccionarioN[i]
print(diccionarioD)

print('')
max_key = max(diccionarioD, key=diccionarioD.get)
print(f'El mes que mas dinero se ha ahorrado es: {max_key}, con un ahorro total de {diccionarioD[max_key]}')

print('')
gastoTotal = sum(diccionarioN.values())
print(f'El gasto total anual es: {gastoTotal * -1}')

print('')
mediaPorMes = gastoTotal/12
print(f'El gasto anual medio a razon de 12 meses es: {mediaPorMes*-1}')


print('')
ingresosTotales = sum(diccionarioP.values())
print(f"Los ingresos anuales son: {ingresosTotales}")

# Imprimir el Grafico.
for key,value in df.iteritems():
    for i in range(0, 100):
        if (value[i]) < 0:
                df.at[i, key] = 0
result = df.head(100)
result.replace(0, np.nan).plot()

print('')
plot.show()