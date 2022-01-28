import pytest
import operaciones

def test_suma():
    x = 3
    y = 2
    resultado = 5
    assert resultado == operaciones.suma(x,y)

def test_division():
    x = 4
    y = 2
    resultado = 2
    assert resultado == operaciones.division(x,y)

def test_resta():
    x = 3
    y = 2
    resultado = 1
    assert resultado == operaciones.resta(x,y)

def test_multiplicacion():
    x = 3
    y = 2
    resultado = 6
    assert resultado == operaciones.multiplicacion(x,y)

def test_elevar():
    base = 2
    exponente = 8
    resultado = 256
    assert resultado == operaciones.elevarNumero(base, exponente)

def test_minimo():
    lista_numeros = [1, 2, 4, 17, -2, 8, -9]
    assert operaciones.minimo(lista_numeros) == -9

def test_es_par():
    assert operaciones.es_par(2)==True
    assert operaciones.es_par(3)==False

def test_operacion_inventada():
    assert operaciones.operacion_inventada(6,1)==6
    assert operaciones.operacion_inventada(6,2)==2