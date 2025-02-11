def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def divide(a, b):
    """Retorna a divisão de dois números. Lança erro se tentar dividir por zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b
