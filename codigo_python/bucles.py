def run():
    LIMITE = 1000000
    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es iguala: ' + str(potencia_2))
        ## print(f'base: 2 potencia: {potencia_2}')
        contador = contador + 1
        potencia_2 = 2 ** contador

if __name__ == '__main__':
    run()