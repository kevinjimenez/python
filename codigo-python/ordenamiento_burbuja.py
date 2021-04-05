import random

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1): ## O(n) * O(n) = O(n*n) = O(n**2)
            if lista[j] > lista[j + 1]:
                lista[j],lista[j + 1] = lista[j+1],lista[j]
    return lista

if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamanio_lista)]
    print(lista)
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)
    ## IF DE UNA LINEA <bloque codigo si cumple> if <condicion> else <bloque codigo si no cumple>
    ## print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    