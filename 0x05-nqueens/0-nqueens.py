#!/usr/bin/python3
"""
0. N queens
"""
import sys


def validate_integer(number):
    """

    """
    try:
        # Intentamos convertir el argumento a entero
        number = int(number)
        # Si la conversión fue exitosa, retornamos el número
        return number
    except ValueError:
        # Si la conversión falló, significa que el argumento no es un entero
        # Entonces retornamos 1
        return 1
    except TypeError:
        # Si ocurre un TypeError, significa que el argumento es None
        # Entonces también retornamos 1
        return 1


# Obtenemos el número de argumentos y los argumentos
argc = len(sys.argv)
argv = sys.argv

# Verificamos si se han proporcionado dos argumentos
if argc != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Verificamos si el argumento N es un entero
n = validate_integer(argv[1])
print()
if n is str:
    print("N must be a number")
    sys.exit(1)

# Verificamos si N es mayor o igual a 4
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Si llegamos aquí, significa que los argumentos son válidos
# Podemos continuar con el programa...

result = []
board = [[0 for j in range(n)] for i in range()]
count = 0

for row in board:
    result.append(row)
    count += 1
    if count % 4 == 0:
        print('\n')

print(result)
