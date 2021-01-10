suma1 = 1 + 2
# suma2 = 1  3.0
# suma3  = 5 / 'platzi'
suma3  = 5 * 'platzi'
print(suma1)
# print(suma2)
print(suma3)
print('hola, mundo')

# Objetos, tipos. escalares y no escalares
suma_string = 'platzi' + 'rocks!'
print(suma_string)
type(suma_string)
print(type(suma_string))
# suma = 6 // 2
suma = 6 / 4 
print(suma)
# reaccionar
# =>>>>>>>>>> gargabe collector
my_var = 'hello platzi' # punta a un lugar de memoria
print(my_var)
my_var = 3+2 # apunta a otro lugar de memoria
print(my_var)

# CADENAS
suma_string = '123'
print(suma_string)
suma_string = '123' * 3
print(suma_string)
suma_string = '123' + '456'
print(suma_string)
suma_string = ('hip' * 3) + 'hurra'
print(suma_string)
suma_string = f'{"hola"}'
print(suma_string)

my_string = 'platzi'
print(len(my_string))
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[2:]) #inicio:final:saltos
print(my_string[:3]) # el final no es inclusivo el inicio si
print(my_string[::2]) # salto en 2 en 2
# my_string = 'yo amo a '+ my_string
# print(my_string)
my_string = f'yo amo a {my_string}, ' * 100 
print(my_string)
# inputs

nombre = input('Cual es tu nombre: ')
print('tu nombre es:', nombre)
print(f'Tu nombre es {nombre}')
edad = int(input('Cual es tu edad: '))
print(type(edad))
print('******************************RETO 1************************')
nombre_string = input('Cual es tu nombre: ')
saludo = f'Bienvenido {nombre_string}'
longitud_nombre = f'La longitud de tu nombre es: {len(nombre_string)}'
print(f'{saludo} \n {longitud_nombre}')
print('************************************************************')

# PROGRAMAS RAMIFICADOS