
import re

def extraer_componentes(operacion):
    # Expresión regular para extraer factores y operador
    match = re.match(r'(\d+)\s*([\+\-\*/])\s*(\d+)', operacion)
    if match:
        factor1, operador, factor2 = match.groups()
        return factor1, operador, factor2
    else:
        return None, None, None
op=input("operacion:")

factor1, operador, factor2 = extraer_componentes(op)

def multiplicacion(a,b):
    return a*b

def division(a, b):
    if b != 0:
        return a / b
def resta(a, b):
    return a - b

def calcular_resultado(factor1, operador, factor2):
    # Convertir los factores a números enteros
    num1 = int(factor1)
    num2 = int(factor2)
    
    if operador == '+':
        return (num1, num2)
    elif operador == '-':
        return resta(num1, num2)
    elif operador == '*':
        return multiplicacion(num1, num2)
    elif operador == '/':
        return division(num1, num2)
    else:
        return "Operador no reconocido"
