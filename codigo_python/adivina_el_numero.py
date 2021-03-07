import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = input('Elige un numero del 1 al 100: ')
    numero_elegido = int(numero_elegido)
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Elige uno mas grande')
            numero_elegido = int(input('Elige otro: '))
        else:
            print('Elige uno mas pequenio')
            numero_elegido = int(input('Elige otro: '))
    print('Ganaste')


if __name__ == '__main__':
    run()