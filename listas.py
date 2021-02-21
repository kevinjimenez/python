my_list = [1,2,3]
print(my_list[0])

# metos para poder obtener el valor => slides
print(my_list[1:])

my_list.append(4)
print(my_list)

my_list[0] = 'a' # reasignacion de valor
print(my_list)

elemento_borrado = my_list.pop()
print(elemento_borrado)
print(my_list)



for element in my_list:
    print(element)

# efectos secundarios
a = [1,2,3]
b = a # la misma lista  tiene los nombre a y b, estan aputado a la misma lista

print(id(a))
print(id(b))

c = [a, b]
print(c)
a.append(5)
print(a)
print(c)

## CLONACION

a = [1,2,3]
print(id(a))
b = a
print(id(b))
c = list(a) ## con la plabra list se clona la lista
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))

d = a[::] # empieza desde el incio hasta el final y salta de uno en uno
print(d)
print(id(d))

# LIST COMPREHENSION

my_list = list(range(100))
print(my_list)

double = [i * 2 for i in my_list] # mutacion cada elemento de la list
print(double)
pares = [i for i in my_list if i % 2 == 0] # filtro numero pares
print(pares)

