def count_words(text: str) -> dict:
    # Convertir el texto a minúsculas para hacer el conteo insensible a mayúsculas/minúsculas
    text = text.lower()
    # Dividir el texto en palabras
    words = text.split()
    # Crear un diccionario para el conteo de palabras
    word_count = {}

    # Recorrer cada palabra en la lista de palabras
    for word in words:
        # Eliminar signos de puntuación alrededor de la palabra
        word = word.strip('.,!?')
        # Si la palabra ya está en el diccionario, aumentar su conteo, de lo contrario, agregarla al diccionario
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


input_text = "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. Si amas lo que haces, tendrás éxito"
print(count_words(input_text))
