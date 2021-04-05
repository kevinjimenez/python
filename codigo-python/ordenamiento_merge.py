import random

def ordenamiento_por_merge(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)
        # llamda recursiva cada mitas
        ordenamiento_por_merge(izquierda)
        ordenamiento_por_merge(derecha)
        # iteradores para recorrer la sublistas
        i = 0
        j = 0
        # iterador para recorrer la lista principal
        k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamanio_lista)]
    print(lista)
    print('-' * 20)
    lista_ordenada = ordenamiento_por_merge(lista)
    print(lista_ordenada)
    ## IF DE UNA LINEA <bloque codigo si cumple> if <condicion> else <bloque codigo si no cumple>
    ## print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')