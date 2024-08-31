def calculadora():
    while True:
        operacion = input("Ingrese la operación (por ejemplo, 2 + 2) o 'c' para borrar: ")

        if operacion == 'c':
            print("Operación borrada.")
            continue

        try:
            resultado = eval(operacion)
            print("Resultado:", resultado)
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
        except Exception as e:
            print("Error en la operación:", e)

if __name__ == "__main__":
    calculadora()
