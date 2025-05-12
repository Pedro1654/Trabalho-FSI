import pytest

from Calculadora import calcular

def test_soma():
    assert calcular(2, 3, '+') == 5

def test_subtracao():
    assert calcular(5, 3, '-') == 2

def test_multiplicacao():
    assert calcular(4, 2, '*') == 8

def test_divisao():
    assert calcular(10, 2, '/') == 5

def test_potencia_positiva():
    assert calcular(2, 3, '^') == 8

def test_potencia_negativa():
    assert calcular(2, -3, '^') == 0.125

def test_divisao_resultado_zero():
    assert calcular(0, 5, '/') == 0

def test_potencia_negativa_inteira():
    assert calcular(-5, 2, '^') == 25

def test_potencia_negativa_impar():
    assert calcular(-5, 3, '^') == -125
# Dividir por 0
def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        calcular(5, 0, '/')

# Testa operadores
@pytest.mark.parametrize("op", ['%', '&', '=', '', '++'])
def test_operador_invalido(op):
    with pytest.raises(ValueError):
        calcular(2, 2, op)

# Testa NaN
import math

def test_nan_primeiro_numero():
    with pytest.raises(ValueError):
        calcular(float('nan'), 5, '+')

def test_nan_segundo_numero():
    with pytest.raises(ValueError):
        calcular(5, float('nan'), '+')

# Testa infinitos
def test_infinito_comum():
    assert math.isinf(calcular(float('inf'), 1, '*'))

def test_divisao_por_infinito():
    assert calcular(1, float('inf'), '/') == 0.0

def test_infinito_negativo():
    assert calcular(1, float('-inf'), '+') == float('-inf')
