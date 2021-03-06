def conversor(tipo_pesos, valor_dolares):
    pesos = input('¿Cuantos pesos '+ tipo_pesos +' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolares
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + " dolares")
    print(f'Tienes ${dolares} dolares')

menu = """
Bienvenido al conversor de monedas 🤑

1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opcion: """

opcion = input(menu)


if opcion == '1':
    conversor('colombianos', 3875)
elif opcion=='2':
    conversor('argentinos', 65)
elif opcion == '3':
    conversor('mexicanos', 24)
else:
    print('Ingrese una opcion')





