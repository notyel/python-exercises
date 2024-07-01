# Ejercicio de Secuencia de Fibonacci

Este ejercicio tiene como objetivo generar la secuencia de Fibonacci hasta un número dado por el usuario.

---

### ¿Qué es la Secuencia de Fibonacci?

La secuencia de Fibonacci es una serie de números en la que cada número (después de los dos primeros) es la suma de los dos anteriores. Comienza típicamente con 0 y 1. La secuencia sigue así:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Es una secuencia matemática que aparece en muchas áreas de las matemáticas y la ciencia, incluidas la biología, la informática y la teoría de números. La relación entre los números de Fibonacci también está estrechamente relacionada con el número áureo, que es aproximadamente 1.618.

---

## Descripción

La función `fibonacci_sequence(n: int) -> list` toma un número entero positivo como entrada y devuelve una lista con los primeros `n` números de la secuencia de Fibonacci.

### Ejemplo de uso

```python
>>> fibonacci_sequence(5)
[0, 1, 1, 2, 3]
>>> fibonacci_sequence(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Uso en un script

El script solicita al usuario un número entero positivo `n` y muestra los primeros `n` números de la secuencia de Fibonacci.

```python
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
```

Este ejercicio es útil para practicar el manejo de listas, ciclos `while` y la interacción con el usuario a través de la entrada estándar.
