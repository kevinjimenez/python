num_1 = int(input('Escoja un numero: '))
num_2 = int(input('Escoja otro numero: '))
if num_1 > num_2:
    print('primer numero mayor q el segundo')
elif num_1 < num_2:
    print('primer numero menor q el segundo')
else:
    print('primer numero es igual al segundo')

print('******************* RETO 2 ********************')
nombre_usuario_uno = input('Ingrese el nombre del usuario uno: ')
edad_usuario_uno = int(input('Ingrese la edad del usuario uno: '))
nombre_usuario_dos = input('Ingrese el nombre del usuario dos: ')
edad_usuario_dos = int(input('Ingrese la edad del usuario dos: '))
if edad_usuario_uno > edad_usuario_dos:
    print(f'El usuario {nombre_usuario_uno} tiene una edad de: {edad_usuario_uno}, y es MAYOR al usuario {nombre_usuario_dos} q tiene una edad de: {edad_usuario_dos}')
elif edad_usuario_uno < edad_usuario_dos:
    print(f'El usuario {nombre_usuario_uno} tiene una edad de: {edad_usuario_uno}, y es MENOR al usuario {nombre_usuario_dos} q tiene una edad de: {edad_usuario_dos}')
else:
    print(f'El usuario {nombre_usuario_uno} tiene una edad de: {edad_usuario_uno}, son de la MISMA EDAD  q el usuario {nombre_usuario_dos} q tiene una edad de: {edad_usuario_dos}')
print('*******************************************')