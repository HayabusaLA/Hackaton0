
def suma(a, b):
    """Función para sumar dos números."""
    return a + b

def main():
    import re

    while True:
        operacion = input("Introduce una operación (o 'c' para borrar, 'q' para salir): ").strip()

        if operacion.lower() == 'q':
            print("Saliendo de la calculadora.")
            break

        if operacion.lower() == 'c':
            print("Operación borrada.")
            continue

        try:
            if re.match(r'^[0-9+\-*/().\s]+$', operacion):
                resultado = eval(operacion)
                print(f"Resultado: {resultado}")
            else:
                print("Entrada no válida. Por favor, introduce una operación matemática válida.")
        except Exception as e:
            print(f"Error al calcular la operación: {e}")

if __name__ == "__main__":
    main()
