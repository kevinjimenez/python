import random

def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    return lista

if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamanio_lista)]
    print(lista)
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)
    ## IF DE UNA LINEA <bloque codigo si cumple> if <condicion> else <bloque codigo si no cumple>
    ## print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')