my_tupla = ()
print(type(my_tupla))

my_tupla = (1, 'dos', True)
# se puede aceder a valores de la tupla x el indice
print(my_tupla[0])
print(my_tupla[1])
print(my_tupla[2])
# no se puede mutar l tupla
# my_tupla[0] = 2

# si la tupla contiene un valor el tipo sera de dicho valor, 
# para crear una tupla debe usarse una coma 
my_tupla = (1) 
print(type(my_tupla))

my_tupla = (1,) 
print(type(my_tupla))

my_other_tuple = (2,3,4)
my_tupla += my_other_tuple # reasignamos una tupla con los valores de other_tuple
print(my_tupla)

# desempaquetar tuplas
x, y, z = my_other_tuple
print(x)
print(y)
print(z)

# funciones y tuplas
def coordenadas():
    return (5,4)
x,y = coordenadas()
print(x)
print(y)