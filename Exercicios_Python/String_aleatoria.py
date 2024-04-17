import random

def embaralhar_string(texto):
    caracteres = list(texto)
    random.shuffle(caracteres)
    return ''.join(caracteres)

minha_string = "Python"
string_embaralhada = embaralhar_string(minha_string)

print(f"A string original: {minha_string}")
print(f"A string embaralhada: {string_embaralhada}")