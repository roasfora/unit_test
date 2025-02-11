import pytest
from src.calculadora import soma, divide    

def test_soma():
    assert soma(2,3) == 5
    assert soma(-1,1) == 0
    assert soma(0,0) == 0

def test_divide():
    assert divide(10,2) == 5
    

def test_divisao_por_zero():
    with pytest.raises(ValueError, match = "Não é possível dividir por zero"):
        divide(10,0)   