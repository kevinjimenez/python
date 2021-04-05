import random

def busqueda_binaria(lista, comienzo, final, objetivo, contador):
    print(f'busacando {objetivo}, entre {lista[comienzo]} y {lista[final-1]}')
    contador+=1
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2 # residuo solo da enteros
    if lista[medio] == objetivo:
        print(contador)
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador)


if __name__ == '__main__':
    tamanio_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))
    lista = sorted([random.randint(0, 100) for i in range(tamanio_lista)])
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo, 0)
    print(lista)
    ## IF DE UNA LINEA <bloque codigo si cumple> if <condicion> else <bloque codigo si no cumple>
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    