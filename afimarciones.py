# asert <expresion booleana>, <mensaje de error>

def primera_letra(lista_de_palabras):
    primeras_letra = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'no se permiten str vacios'

        primeras_letra.append(palabra)
    
    return primeras_letra

palabras = ['kevin', 'aa', 'bb', 'alisson']
print(primera_letra(palabras))