def morral(tamanio_morral, pesos, valores, n): ##n indice sobre cual se esta trabajando
    if n == 0 or tamanio_morral == 0:
        return 0

    if pesos[n - 1] > tamanio_morral:
        print(pesos[n - 1])
        return morral(tamanio_morral, pesos, valores, n - 1)

    # print(valores[n-1] + morral(tamanio_morral - pesos[n-1], pesos, valores, n - 1))
    # print(tamanio_morral, pesos, valores, n - 1)
    return max(valores[n-1] + morral(tamanio_morral - pesos[n-1], pesos, valores, n - 1),
        morral(tamanio_morral, pesos, valores, n - 1))

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10,20,30]
    tamanio_morral = 50
    n = len(valores)

    resultado = morral(tamanio_morral, pesos, valores, n)
    print(resultado)