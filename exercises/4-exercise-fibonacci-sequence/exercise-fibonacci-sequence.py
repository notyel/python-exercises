def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:n]


# Solicitar al usuario el número de elementos de la secuencia
n = int(input("Introduce un número entero positivo: "))

# Verificar si el número es positivo
if n <= 0:
    print("Por favor, introduce un número entero positivo.")
else:
    # Generar y mostrar la secuencia de Fibonacci
    fib_sequence = fibonacci_sequence(n)
    print(f"Los primeros {n} números de la secuencia de Fibonacci son:")
    print(fib_sequence)
