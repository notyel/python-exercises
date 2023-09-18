# Función para verificar si una palabra es un palíndromo
def is_palindrome(word: str) -> bool:
    word = word.lower().replace(" ", "")
    return word == word[::-1]


# Explicación de la función is_palindrome
"""
Esta función toma una palabra como entrada y verifica si es un palíndromo,
lo que significa que se lee igual de izquierda a derecha y de derecha a izquierda.
Primero, convierte la palabra a minúsculas y elimina los espacios en blanco.
Luego, compara la palabra original con su versión invertida y devuelve True si es un palíndromo,
o False en caso contrario.
"""

# Ejemplos de palabras y si son palíndromos o no
print("Abba", is_palindrome("Abba"))  # Palíndromo
print("Reconocer", is_palindrome("Reconocer"))  # Palíndromo
print("Amo la paloma", is_palindrome("Amo la paloma"))  # No es un palíndromo
print("Hola Mundo", is_palindrome("Hola Mundo"))  # No es un palíndromo
