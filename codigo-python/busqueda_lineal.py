import random

def busqueda_lineal(lista, objetivo):
    match = False ## O(1)

    for elemento in lista:        ## O(n)
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    lista = [random.randint(0, 100) for i in range(tamanio_lista)] 
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    ## IF DE UNA LINEA <bloque codigo si cumple> if <condicion> else <bloque codigo si no cumple>
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    