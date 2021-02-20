def suma(a, b):
    total = a+b
    return total

totalSuma = suma(2,3)
print(totalSuma)

## funcuiones con parametors con valor por default
def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido}{nombre}'
    else:
        return f'{nombre}{apellido}'
primero = nombre_completo('kevin', 'jimenez')
print(primero)
# una forma de mandar los parametros
primero2 = nombre_completo('kevin', 'jimenez', True)
print(primero2)
# el parametro 3 es opcional ya que contiene un valor por default
primero3 = nombre_completo('kevin', 'jimenez')
print(primero3)
# podemos saltarnos el order
primero4 = nombre_completo(apellido='jimenez', inverso=True, nombre='kevin')
print(primero4)

################### FUNCION DE SACAR RAIZ #############################
def aproximacion(objetivo, epsilon = 0.001):
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    # print(abs(respuesta**2 - objetivo),  respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'no se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'la raiz cuadrada {objetivo} es {respuesta}')

def enumeracion_exhaustiva(objetivo):    
    respuesta = 0
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'la raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'el {objetivo} no tiene una raiz cuadrada exacta')
    
def busqueda_binaria(objetivo, epsilon = 0.001):   
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2

    print(f'la raiz cuadrada de {objetivo} es {respuesta}')

def menu_metodos():
    print(f'1.- aproximacion \n 2.- enumeracion exhaustiva \n 3.- busqueda binaria')
    opcion = input('Ingrese la opción: ')
    if opcion == "1":
        objetivo = int(input('Ingrese el objetivo: '))
        aproximacion(objetivo)
    if opcion == "2":
        objetivo = int(input('Ingrese el objetivo: '))
        enumeracion_exhaustiva(objetivo)
    if opcion == "3":
        objetivo = int(input('Ingrese el objetivo: '))
        busqueda_binaria(objetivo)

menu_metodos()