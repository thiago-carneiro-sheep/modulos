# Modulo operações matemáticas

def sum(x, y):
    """Retorna a soma de x e y."""
    return x + y

def subtract(x, y):
    """Retorna a subtração de x e y."""
    return x - y

def multiply(x, y):
    """Retorna a multiplicação de x e y."""
    return x * y

def divide(x, y):
    """Retorna a divisão de x e y."""
    if y != 0:
        return x / y
    else:
        raise ValueError("O denominador não pode ser zero.")