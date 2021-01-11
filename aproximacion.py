objetivo = int(input('Escoge un entero: '))
epsilon = 0.0001 # cuanto preciso queremos q sea
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    # print(abs(respuesta**2 - objetivo),  respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'no se encontro la raiz cuadrada {objetivo}')
else:
    print(f'la raiz cuadrada {objetivo} es {respuesta}')