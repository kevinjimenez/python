my_dict = {
    'kevin': 35,
    'alisson': 26,
    'katy': 19,
}

print(my_dict)
print(my_dict['alisson'])

# obtener un valor sin conocer la llave, 
# si no la tiene retorna el valor q se ingreso en el .get()
print(my_dict.get('orlando', 30))
print(my_dict.get('kevin', 30))

## reasignar el valor de una llave
my_dict['alisson'] = 25
print(my_dict)

# agregar nueva llave y valor
my_dict['juan'] = 26
print(my_dict)

# eliminar llave
del my_dict['kevin']
print(my_dict)

# iterar diccionario

# llaves
for llave in my_dict.keys():
    print(llave)

# values
for valor in my_dict.values():
    print(valor)

# llave y valor
for llave, valor in my_dict.items():
    print(llave, valor)

# existe llave dentro diccionario 
print('kevin' in my_dict)
print('alisson' in my_dict)

# DICCIONARIO COMPREHENSION
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(type(dict1.items()))
print(dict1.keys())
print(dict1.items())
# dict_variable = {key:value for (key,value) in dictonary.items()}
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)

### mutar diccionario 
my_dict_mutado = {llave: valor + 2 for llave, valor in my_dict.items()}
print(my_dict_mutado)

## filtro diccionario
my_dict_pares = {llave: valor  for llave, valor in my_dict.items() if valor % 2 == 0}
print(my_dict_pares)

