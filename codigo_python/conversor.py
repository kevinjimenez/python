pesos = input('¿Cuantos pesos colombianos tienes?: ')
pesos = float(pesos)
valor_dolares = 3875
dolares = pesos / valor_dolares
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes $' + dolares + " dolares")
print(f'Tienes ${dolares} dolares')
