import pytest
import Actividad2



def test_DiccionarioP():
    resultado = {'Enero': 29685, 'Febrero': 24437, 'Marzo': 21721, 'Abril': 15200, 'Mayo': 27504, 'Junio': 22720, 'Julio': 26690, 'Agosto': 20278, 'Septiembre': 18203, 'Octubre': 26369, 'Noviembre': 25337, 'Diciembre': 22817}
    assert resultado == Actividad2.diccionarioP

def test_diccionarioN():
    resultado = {'Enero': -17621, 'Febrero': -24398, 'Marzo': -29690, 'Abril': -34133, 'Mayo': -17200, 'Junio': -24197, 'Julio': -18390, 'Agosto': -29013, 'Septiembre': -29151, 'Octubre': -22957, 'Noviembre': -24180, 'Diciembre': -25861}
    assert resultado == Actividad2.diccionarioN

def test_diccionarioD():
    resultado = {'Enero': 12064, 'Febrero': 39, 'Marzo': -7969, 'Abril': -18933, 'Mayo': 10304, 'Junio': -1477, 'Julio': 8300, 'Agosto': -8735, 'Septiembre': -10948, 'Octubre': 3412, 'Noviembre': 1157, 'Diciembre': -3044}
    assert resultado == Actividad2.diccionarioD

def test_mesConMasGasto():
    mes = 'Abril'
    gasto = -34133
    assert mes, gasto == Actividad2.mesConMasGasto()

def test_mesConMasAhorro():
    mes = 'Enero'
    ahorro = 12064
    assert mes, ahorro == Actividad2.mesConMasAhorro()

def test_gastoAnual():
    gasto = -296791
    assert gasto == Actividad2.gastoAnual()

# Calcular el gasto medio anual.
def test_gastoMedio():
    gasto = -24732.583333333332
    assert gasto == Actividad2.gastoMedio()

#Calcular los ingresos totales anuales.
def test_ingresosTotales():
    total = 280961
    assert total == Actividad2.ingresosTotales()