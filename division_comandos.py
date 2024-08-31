def division(a, b):
    """
    Divide dos números.

    Args:
    a (float): El dividendo.
    b (float): El divisor.

    Returns:
    float: El resultado de dividir a entre b.

    Raises:
    ValueError: Si b es 0, se lanza un error para evitar la división por cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

# Ejemplo de uso:
try:
    resultado_division = division(10, 2)
    print("Resultado de la división: ", resultado_division)
except ValueError as e:
    print(e)
